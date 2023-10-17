from index.extensions.jalali_converter import jalali_converter as jConvert
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.images.api.fields import ImageRenditionField
from wagtail.models import Page, PageManager, Orderable
from user_accounts.models import user_accounts as User
from wagtail.snippets.models import register_snippet
from wagtail_color_panel.fields import ColorField
from django.db.models import PROTECT, SET_NULL
from django.shortcuts import render, redirect
from wagtail.fields import RichTextField
from rest_framework.fields import Field
from django.utils import timezone
from django.db.models import Sum
from wagtail.api import APIField
from django.db import models
from django import forms
import pandas as pd


class ProductPageManager(PageManager):
    '''Inventory & Products Manager'''
    pass

class InventoryItemPageManager(PageManager):
    '''Inventory & Products Manager'''
    pass

# Product Index Child Serializer
class ProductChildPageSerializer(Field):
    ''' Serialize model => API | JSON '''
    def to_representation(self, value):
        return [
            {
                'id' : child.id,
                'slug' : child.slug,
                'title' : child.title,
                'product_title' : child.product_title,
                'comments' : child.comments,
                'author' : child.author,
                'image' : child.image,
                'quantity' : child.quantity,
                'date' : child.date,
                'brand' : child.brand,
                'price' : child.price,
                'short_description' : child.short_description,
                'description' : child.description,
                'colors' : child.colors,
                'is_active' : child.is_active,
                'is_available' : child.is_available,
                'total_visits' : child.total_visits,
                'collection' : child.collection,

            }for child in value
        ]


class ProductSlide(Orderable):
    ''' Product slide '''
    product_slide = ParentalKey("product.InventoryItem", related_name="PRODUCT_SLIDE")
    slide_title = models.CharField(max_length=14, verbose_name='عنوان اسلاید', db_index=True,)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=False, blank=False,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name='تصویر اسلاید',
        help_text='تصویر اسلاید را وارد نمایید',
    )
    slide_desc = models.CharField(max_length=35, verbose_name='توضیحات', null=True, blank=True)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='مجموعه برای رنگ بندی انتخاب کنید',
    )

    panels = [
        FieldPanel('slide_title'),
        FieldPanel('image'),
        FieldPanel('slide_desc'),
        FieldPanel('collection'),
        ]

    api_fields = [
        APIField('slide_title'),
        APIField('image'),
        APIField('slide_desc'),
        APIField('collection'),
        APIField('image', serializer=ImageRenditionField('fill-250x280')),
    ]

    def __str__(self):
        return self.color_title

    class Meta:
        verbose_name = 'اسلاید تصاویر محصول'
        verbose_name_plural = 'اسلاید تصاویر محصول'


class ProductColor(Orderable):
    ''' Product Color '''
    product_color = ParentalKey("product.InventoryItem", related_name="PRODUCT_COLORS")
    color_title = models.CharField(max_length=14, verbose_name='نام رنگ بندی', db_index=True,)
    color = ColorField()
    pquantity = models.IntegerField(verbose_name='تعداد رنگ بندی :')
    color_des = models.CharField(max_length=35, verbose_name='توضیحات', null=True, blank=True)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='مجموعه برای رنگ بندی انتخاب کنید',
    )

    panels = [
        FieldPanel('color_title'),
        NativeColorPanel('color'),
        FieldPanel('pquantity'),
        FieldPanel('color_des'),
        FieldPanel('collection'),
        ]

    api_fields = [
        APIField('color_title'),
        APIField('color'),
        APIField('pquantity'),
        APIField('color_des'),
        APIField('collection'),
    ]

    def __str__(self):
        return self.color_title

    class Meta:
        verbose_name = 'رنگ بندی'
        verbose_name_plural = 'رنگ بندی محصولات'


class ProductOffer(Orderable):
    ''' Product Offer '''
    product_offer = ParentalKey("product.InventoryItem", related_name="PRODUCT_OFFER")
    offer_title = models.CharField(max_length=14, verbose_name='عنوان تخفیف', db_index=True,)
    value = models.PositiveIntegerField(verbose_name='قیمت جدید محصول')
    offer_des = models.CharField(max_length=35, verbose_name='توضیحات تخفیف', null=True, blank=True)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='مجموعه برای تخفیف انتخاب کنید',
    )

    panels = [
        FieldPanel('offer_title'),
        FieldPanel('value'),
        FieldPanel('offer_des'),
        FieldPanel('collection'),
        ]

    api_fields = [
        APIField('offer_title'),
        APIField('value'),
        APIField('offer_des'),
        APIField('collection'),
    ]

    def __str__(self):
        return self.offer_title

    class Meta:
        verbose_name = 'محصول تخفیف دار'
        verbose_name_plural = 'محصولات تخفیف دار'


class ProductIndex(RoutablePageMixin, Page):
    ''' PRODUCT INDEX PAGE '''

    intro = RichTextField(blank=True, verbose_name='نام صفحه محصولات سایت')

    description = models.TextField(verbose_name='توضیجات', db_index=True, null=True, blank=True)

    keywords = models.TextField(verbose_name='کلید واژه صفحه محصولات', db_index=True, null=True, blank=True)

    objects = ProductPageManager()

    max_count = 1

    subpage_types = ['product.InventoryItem']

    parent_page_types = ['index.Index']

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('description'),
        FieldPanel('keywords'),
    ]

    api_fields = [
        APIField("get_child_pages", serializer=ProductChildPageSerializer()),
    ]

    @property
    def get_child_pages(self):
        return self.get_children().public().live()

    def get_template(self, request, *args, **kwargs):

        return 'products/productarchive/productarchive.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        loaded_product = InventoryItem.objects.live().public().order_by('-first_published_at')
        context['products'] = loaded_product if loaded_product is not None else 0
        return context

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs),
        )

    class Meta:
        verbose_name = 'صفحه محصولات'


@register_snippet
class Discount(models.Model):
    title = models.CharField(max_length=50, unique=True)
    DISCOUNT_TYPES = (
        ('percentage', 'درصدی'),
        ('fixed', 'ثابت'),
    )
    code = models.CharField(max_length=50, unique=True)
    dis_type = models.CharField(max_length=20, choices=DISCOUNT_TYPES, verbose_name='نوع اعمال تخفیف')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(
        'product.InventoryItem',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='انتخاب محصول برای اعمال کد تخفیف',
    )
    collection = models.ForeignKey(
        'category.CategoryProduct',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='انتخاب دسته بندی برای اعمال کد تخفیف',
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def check_dis(self,code):
        if code == self.code :
            return True
        else:
            return False

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'


class InventoryItem(RoutablePageMixin, Page):
    ''' Inventory => &&& <= Products '''
    shenase = models.CharField(max_length=300, verbose_name='شناسه محصول',null=False, blank=False )
    product_title = models.CharField(max_length=300, verbose_name='نام و مدل محصول', null=True, blank=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    keywords = models.TextField(verbose_name='کلید واژه محصول', db_index=True, null=True, blank=True)
    description = RichTextField(verbose_name='درباره محصول', db_index=True, null=True, blank=True)
    comments = models.ManyToManyField('index.Comments', blank=True)
    collection = ParentalManyToManyField(
        'category.CategoryProduct',
        null=True,
        blank=True,
        help_text='مجموعه برای محصول انتخاب کنید',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=False, blank=False,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name='تصویر شاخص محصول',
        help_text='تصویر شاخص محصول را اضافه کنید',
    )
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول', null=True)
    date = models.DateTimeField("Post date", default=timezone.now)
    brand = models.ForeignKey(
        'brand.BrandPage',
        null=False, blank=False,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name='برند محصول',
        help_text='یک برند برای محصول انتخاب کنید',
    )
    price = models.PositiveIntegerField(verbose_name='قیمت', blank=False, null=False)
    short_description = RichTextField(max_length=320, null=True, blank=True, verbose_name='توضیحات کوتاه')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال', blank=False, null=False)
    is_available = models.BooleanField(default=True, verbose_name='موجودی / عدم موجودی', blank=False, null=False)
    product_type = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='نوع محصول')
    product_jense = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='جنس محصول')
    product_wight = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='وزن محصول')
    product_abad = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='ابعاد خارجی محصول')
    product_size = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='سایز محصول')
    product_garr = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='گارانتی محصول')
    total_visits = models.IntegerField(verbose_name='تعداد کل بازدید', default=0)
    
    objects = InventoryItemPageManager()

    subpage_types = []

    parent_page_types = ['product.ProductIndex']

    content_panels = Page.content_panels + [
        FieldPanel('shenase'),
        FieldPanel('product_title'),
        FieldPanel('brand'),
        FieldPanel('keywords'),
        FieldPanel('price'),
        FieldPanel('image'),
        MultiFieldPanel([
            InlinePanel("PRODUCT_SLIDE", max_num=5, label="تصویر محصول"),
        ], heading="انتخاب اسلاید تصاویر برای محصول"),
        MultiFieldPanel([
            InlinePanel("PRODUCT_COLORS", min_num=1, label="رنگ بندی محصول"),
        ], heading="انتخاب رنگ بندی محصول"),
        FieldPanel('quantity'),
        FieldPanel('short_description'),
        FieldPanel('description'),
        MultiFieldPanel([
            InlinePanel("PRODUCT_OFFER", max_num=1, label="تخفیف محصول"),
        ], heading="افزودن تخفیف به محصول"),
        FieldPanel('is_active'),
        FieldPanel("product_type"),
        FieldPanel("product_jense"),
        FieldPanel("product_wight"),
        FieldPanel("product_abad"),
        FieldPanel("product_size"),
        FieldPanel("product_garr"),
        FieldPanel('collection', widget=forms.CheckboxSelectMultiple),
    ]

    api_fields = [
        APIField('shenase'),
        APIField('product_title'),
        APIField('comments'),
        APIField('collection'),
        APIField('author'),
        APIField('image'),
        APIField('quantity'),
        APIField('date'),
        APIField('brand'),
        APIField('price'),
        APIField('short_description'),
        APIField('description'),
        APIField('PRODUCT_SLIDE'),
        APIField('PRODUCT_COLORS'),
        APIField("product_type"),
        APIField("product_jense"),
        APIField("product_wight"),
        APIField("product_abad"),
        APIField("product_size"),
        APIField("product_garr"),
        APIField('PRODUCT_OFFER'),
        APIField('is_active'),
        APIField('is_available'),
        APIField('total_visits'),
        APIField('image', serializer=ImageRenditionField('fill-250x280')),
    ]

    @property
    def get_child_pages(self):
        return self.get_children().public().live()

    def apply_discount(self, discount_code, price):
        try:
            discount = Discount.objects.get(code=discount_code)
            if discount.start_date <= timezone.now().date() <= discount.end_date:
                if discount.check_dis(discount_code):
                    if discount.dis_type == 'percentage':
                        # تخفیف بر اساس درصد
                        discount_amount = price * discount.value / 100
                    elif discount.dis_type == 'fixed':
                        # تخفیف به صورت مقدار ثابت
                        discount_amount = discount.value
                    else:
                        # نوع تخفیف نامعتبر
                        discount_amount = 0

                    final_price = price - discount_amount
                    return final_price

        except Discount.DoesNotExist:
            pass

        return self.price

    def __str__(self):
        return f"{self.product_title} - {self.quantity} in stock"

    def restock(self, quantity):
        self.quantity += quantity
        if self.quantity > 0:
            self.is_available = True
        self.save()

    restock.short_description = 'شارژ محصول'

    def sell(self, quantity):
        if self.is_available and self.quantity >= quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.is_available = False
            self.save()
            return True
        else:
            return False

    sell.short_description = 'فروش محصول'

    def get_template(self, request, *args, **kwargs):

        return 'products/productsingle/productsingle.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def serve(self, request, *args, **kwargs):
        return render(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs),
        )

    def save(self, *args, **kwargs):
        if not self.is_available:
            self.is_available = False
        super().save(*args, **kwargs)

    save.short_description = 'ذخیره محصول'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        

class Inventory(models.Model):
    products = models.ForeignKey(InventoryItem, blank=True, null=True, on_delete=SET_NULL)

    def sell_product(self, product_id, quantity):
        try:
            product = self.products.get(id=product_id)
            return product.sell(quantity)
        except InventoryItem.DoesNotExist:
            return False

    def restock_product(self, product_id, quantity):
        try:
            product = self.products.get(id=product_id)
            product.restock(quantity)
            return True
        except InventoryItem.DoesNotExist:
            return False

    class Meta:
        verbose_name = 'انبار کالا'
        verbose_name_plural = 'انبار کالا'


class Invoice(models.Model):
    date = models.DateField(default=timezone.now)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    product = models.ForeignKey(InventoryItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)


class ExportManager:
    def export_to_pdf(self):
        products = InventoryItem.objects.all()
        data = {'InventoryItem Name': [], 'Total Sales': [], 'Total Visits': []}
        for product in products:
            data['InventoryItem Name'].append(product.name)
            data['Total Sales'].append(product.get_product_total_sales())
            data['Total Visits'].append(product.get_product_total_visits())

        df = pd.DataFrame(data)
        output_path = 'product_sales.pdf'
        df.to_pdf(output_path)

        return output_path

    def export_to_excel(self):
        products = ProInventoryItemduct.objects.all()
        data = {'InventoryItem Name': [], 'Total Sales': [], 'Total Visits': []}
        for product in products:
            data['InventoryItem Name'].append(product.name)
            data['Total Sales'].append(product.get_product_total_sales())
            data['Total Visits'].append(product.get_product_total_visits())

        df = pd.DataFrame(data)
        output_path = 'product_sales.xlsx'
        df.to_excel(output_path)

        return output_path

ORDER_STATUS = ((0, "در حال پردازش"), (1, "تکمیل شده"), (2, "استرداد"), (3, "لغو شده"), (4, "در انتظار پرداخت"))

SEND_METHOD = ((0, "تحویل حضوری"), (1, "پست پیشتاز"), (2, "پیک"))

class Orders(models.Model):
    shenase = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='شناسه سفارش')
    customer = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='مشتری')
    product = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='محصول')
    number = models.PositiveIntegerField(verbose_name='تعداد', null=True, blank=True)
    color = models.CharField(max_length=30, db_index=True, null=True, blank=True, verbose_name='رنگ')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    status = models.IntegerField(choices=ORDER_STATUS, default=0, verbose_name='وضعیت سفارش')
    date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت')
    send_method = models.IntegerField(choices=SEND_METHOD, default=0, verbose_name='روش ارسال')
    send_price = models.PositiveIntegerField(verbose_name='هزینه ارسال')

    def __str__(self):
        return self.product

    def jpub(self):
        return jConvert(self.date)

    class Meta:
        ordering = ["-date"]
        verbose_name = 'سفارش ثبت شده'
        verbose_name_plural = 'اقلام سفارش'