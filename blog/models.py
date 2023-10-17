"""
2020 Black
developer : #ABS
"""

# Import all requirements
from index.extensions.jalali_converter import jalali_converter as jConvert
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.contrib.routable_page.models import RoutablePageMixin
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.images.api.fields import ImageRenditionField
from user_accounts.models import user_accounts as User
from wagtail.snippets.models import register_snippet
from django.db.models import PROTECT, SET_NULL
from django.shortcuts import render, redirect
from wagtail.models import Page, PageManager
from django.core.paginator import Paginator
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from category.models import CategoryBlog
from rest_framework.fields import Field
from django.utils import timezone
from index.models import Comments
from wagtail.api import APIField
from wagtail.search import index
from django.db import models


# Blog Page Manager
class BlogPageManager(PageManager):
    ''' 
    DEVELOPMENT BY #ABS 
    '''
    pass


# Blog Index Child Serializer
class BlogPageChildSerializer(Field):
    ''' Serialize model => API | JSON '''
    def to_representation(self, value):
        return [
            {
                'id' : child.id,
                'slug' : child.slug,
                'comments' : child.comments,
                'title' : child.title,
                'intro' : child.intro,
                'author' : child.author,
                'image' : child.image,
                'date' : child.date,
                'description' : child.description,
                'collection' : child.collection,

            }for child in value
        ]


# blog app index model
class BlogIndex(Page, RoutablePageMixin):
    intro = RichTextField(blank=True, verbose_name='نام صفحه وبلاگ سایت')

    description = models.TextField(verbose_name='توضیجات', db_index=True, null=True, blank=True)

    keywords = models.TextField(verbose_name='کلید واژه صفحه بلاگ', db_index=True, null=True, blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    max_count = 1
    objects = BlogPageManager()
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('keywords'),
        FieldPanel('description'),
    ]

    subpage_types = ['blog.BlogPage']

    parent_page_types = ['index.Index']

    api_fields = [
        APIField("get_child_pages", serializer=BlogPageChildSerializer()),
    ]
    
    @property
    def get_child_pages(self):
        return self.get_children().public().live()

    def get_template(self, request, *args, **kwargs):
        ajax_template = 'blog/blogarchive/blogarchive.html'
        return ajax_template

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        loaded_post = BlogPage.objects.live().public().order_by('-first_published_at')
        paginator = Paginator(loaded_post, 9)
        page = request.GET.get('page')
        try:
            items = paginator.get_page(page)
        except PageNotAnInteger:
            items = paginator.get_page(1)
        context['posts'] = items if items is not None else 0
        return context

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs),
        )

    class Meta:
        verbose_name = 'صفحه اصلی وبلاگ'


# blog page model
class BlogPage(Page, RoutablePageMixin):
    comments = models.ManyToManyField('index.Comments', blank=True)
    description = models.TextField(verbose_name='توضیجات', db_index=True, null=True, blank=True)
    keywords = models.TextField(verbose_name='کلید واژه مقاله', db_index=True, null=True, blank=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=False, blank=False,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name='تصویر شاخص پست',
        help_text='یک تصویر بارگزاری کنید',
        )
    collection = models.ForeignKey(
        'category.CategoryBlog',
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        help_text='یک دسته بندی انتخاب کنید',
    )
    intro = models.CharField(max_length=25, verbose_name='توضیحات ابتدایی راجب پست')
    date = models.DateTimeField("Post date",default=timezone.now)
    body = RichTextField(blank=True, verbose_name='محتوای پست')

    subpage_types = []

    parent_page_types = ['BlogIndex']

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('image'),
        FieldPanel('intro'),
        FieldPanel('keywords'),
        FieldPanel('description'),
        FieldPanel('collection'),
    ]

    def jpub(self):
        return jConvert(self.date)
    
    jpub.short_description = 'زمان انتشار'

    api_fields = [
        APIField('comments'),
        APIField('title'),
        APIField('body'),
        APIField('intro'),
        APIField('image'),
        APIField('author'),
        APIField('jpub'),
        APIField('description'),
        APIField('collection'),
        APIField('image', serializer=ImageRenditionField('fill-250x150')),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    def get_template(self, request, *args, **kwargs):
        ajax_template = 'blog/blogsingle/blogsingle.html'
        return ajax_template
        
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        category = CategoryBlog.objects.live().public()[:5]
        context['category'] = category
        return context

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs),
        )

    class Meta:
        verbose_name = 'پست وبلاگ'
        verbose_name_plural = 'پست های وبلاگ'
