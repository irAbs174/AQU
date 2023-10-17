"""
2020 Black
developer : #ABS
"""

# Import all requirements
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.snippets.models import register_snippet
from django.shortcuts import render, redirect
from wagtail.models import Page, PageManager
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from rest_framework.fields import Field
from taggit.forms import TagField
from wagtail.api import APIField
from wagtail.search import index
from django.db import models

# INDEX PAGE MANAGER
class IndexPageManager(PageManager):
    '''
    DEVELOPMENT : #ABS
     '''
    pass


# Index class
class Index(Page):
    body = RichTextField(blank=True)
    description = models.TextField(verbose_name='توضیجات', db_index=True, null=True, blank=True)
    keywords = models.TextField(verbose_name='کلید واژه صفحه اصلی', db_index=True, null=True, blank=True)

    objects = IndexPageManager()

    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('keywords'),
        FieldPanel('description'),
    ]

    def get_template(self, request, *args, **kwargs):

        return 'index/index.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs),
        )

    class Meta:
        verbose_name = "خانه"


@register_snippet
class Comments(models.Model):
    user = models.CharField(max_length=25, verbose_name='کاربر نظر دهنده',null=True, blank=True)
    post = models.CharField(max_length=25, verbose_name='پست',null=True, blank=True)
    title = models.CharField(max_length=100,verbose_name='عنوان نظر',null=True, blank=True)
    name = models.CharField(max_length=100,verbose_name='نام نظر دهنده',null=True, blank=True)
    email = models.EmailField(verbose_name='ایمیل نظر دهنده',null=True, blank=True)
    body = models.TextField(verbose_name='نظر',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت نظر',null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'بازخورد کاربر'
        verbose_name_plural = 'بازخورد کاربران'

class Comments_like(models.Model):
    user = models.CharField(max_length=25, verbose_name='کاربر لایک / دیسلایک کننده',null=True, blank=True)
    post = models.CharField(max_length=25, verbose_name='پست لایک/ دیسلایک شده',null=True, blank=True)
    like = models.PositiveIntegerField(verbose_name='مجموع لایک پست',null=True, blank=True)
    dis_like = models.PositiveIntegerField(verbose_name='مجموع دیسلایک پست',null=True, blank=True)

    class Meta:
        verbose_name = 'لایک و دیسلایک'
        verbose_name_plural = 'لایک ها و دیسلایک ها'

class Visit(models.Model):
    visit_count = models.IntegerField(default=0, verbose_name='جمع بازدید', null=True, blank=True)
    last_visit_url = models.CharField(max_length=200, verbose_name='آخرین آدرس بازدید شده', null=True, blank=True)
    ip_address = models.GenericIPAddressField( verbose_name='آدرس آیپی', null=True, blank=True)
    session_key = models.GenericIPAddressField( verbose_name='کلید نشست', null=True, blank=True)
    browser = models.CharField(max_length=200, verbose_name='مروگر', null=True, blank=True)
    browser_version = models.CharField(max_length=200, verbose_name='نسخه مرورگر', null=True, blank=True)
    os = models.CharField(max_length=200, verbose_name='سیستم عامل', null=True, blank=True)
    os_version = models.CharField(max_length=200, verbose_name='نسخه سیستم عامل', null=True, blank=True)
    device = models.CharField(max_length=200, verbose_name='دستگاه', null=True, blank=True)
    country = models.CharField(max_length=70, verbose_name='کشور', null=True, blank=True)
    country_emoji = models.CharField(max_length=70, verbose_name='نماد کشور', null=True, blank=True)
    city = models.CharField(max_length=70, verbose_name='شهر', null=True, blank=True)
    isp = models.CharField(max_length=70, verbose_name='سرویس دهنده', null=True, blank=True)
    current_time = models.CharField(max_length=70, verbose_name='زمان فعلی', null=True, blank=True)
    zip_code = models.CharField(max_length=70, verbose_name='کد پستی', null=True, blank=True)
    last_visit_time = models.DateTimeField(auto_now=True, verbose_name='آخرین سابقه بازدید', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در', null=True, blank=True)

    def increment_visit_count(self):
        self.visit_count += 1
        self.save()

    class Meta:
        verbose_name = 'بازدید'
        verbose_name_plural = 'آمار بازدید'
        
STATUS = ((0, "پیش نویس"), (1, "انتشار"))

class Custom_pages(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='عنوان صفحه', null=False, blank=False)
    slug = models.CharField(max_length=50, unique=True, verbose_name='آدرس صفحه', null=False, blank=False)
    content = models.TextField()
    description = models.CharField(max_length=50, unique=True, verbose_name='توضیحات', null=False, blank=False)
    keywords = models.CharField(max_length=50, unique=True, verbose_name='کلیدواژه ها', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='وضعیت')

    class Meta:
        ordering = ["-created_on"]
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحه ها'

    def __str__(self):
        return self.title