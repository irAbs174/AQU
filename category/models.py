from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.images.api.fields import ImageRenditionField
from user_accounts.models import user_accounts as User
from wagtail.snippets.models import register_snippet
from django.db.models import PROTECT, SET_NULL
from django.shortcuts import render, redirect
from wagtail.models import Page, PageManager
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from django.utils import timezone
from wagtail.api import APIField
from wagtail.search import index
from django.db import models


# Category Page Manager
class CategoryPageManager(PageManager):
    ''' 
    DEVELOPMENT BY #ABS 
    '''
    pass


# Category app index model
class CategoryIndex(Page, RoutablePageMixin):
    intro = RichTextField(blank=True, verbose_name='نام صفحه دسته بندی های سایت')
    description = models.TextField(verbose_name='توضیجات', db_index=True, null=True, blank=True)
    keywords = models.TextField(verbose_name='کلید واژه صفحه دسته بندی ها', db_index=True, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    max_count = 1
    objects = CategoryPageManager()
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('keywords'),
        FieldPanel('description'),
        ]

    subpage_types = ['category.CategoryBlog', 'category.CategoryProduct',]

    parent_page_types = ['index.Index']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_context(request, *args, **kwargs),
        )

    class Meta:
        verbose_name = 'صفحه آرشیو دسته بندی ها'


class CategoryBlog(Page, RoutablePageMixin):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,)
    keywords = models.TextField(verbose_name='کلید واژه دسته بندی مقاله', db_index=True, null=True, blank=True)
    description = models.CharField(max_length=60, verbose_name='توضیحات کامل دسته بندی')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='تصویر شاخص دسته بندی',
        help_text='تصویر شاخص دسته بندی را اضافه کنید',
    )
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='یک مجموعه برای دسته بندی مقاله انتخاب کنید',
    )

    subpage_types = []

    parent_page_types = ['category.CategoryIndex']

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('keywords'),
        FieldPanel('collection'),
        FieldPanel('image'),
    ]

    api_fields = [
        APIField('description'),
        APIField('collection'),
        APIField('image'),
        APIField('image', serializer=ImageRenditionField('fill-250x280')),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('collection'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_context(request, *args, **kwargs),
        )

    class Meta:
        verbose_name = 'دسته بندی وبلاگ'
        verbose_name_plural = 'دسته بندی های وبلاگ'


class CategoryProduct(Page, RoutablePageMixin):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,)
    keywords = models.TextField(verbose_name='کلید واژه دسته بندی محصول', db_index=True, null=True, blank=True)
    description = models.CharField(max_length=60, verbose_name='توضیحات کامل دسته بندی')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='تصویر شاخص دسته بندی',
        help_text='تصویر شاخص دسته بندی را اضافه کنید',
    )
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='یک مجموعه برای دسته بندی محصول انتخاب کنید',
    )

    subpage_types = []

    parent_page_types = ['category.CategoryIndex']

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('keywords'),
        FieldPanel('collection'),
        FieldPanel('image'),
    ]

    api_fields = [
        APIField('description'),
        APIField('collection'),
        APIField('image'),
        APIField('image', serializer=ImageRenditionField('fill-250x280')),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('collection'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_context(request, *args, **kwargs),
        )

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی های محصولات'