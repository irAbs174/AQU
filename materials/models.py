from django.db import models

class Materials(models.Model):
    material_key = models.CharField(max_length=50, verbose_name='کلید',null=True, blank=True )
    material_author = models.CharField(max_length=40, verbose_name='اپراتور ثبت',null=True, blank=True )
    material_name = models.CharField(max_length=300, verbose_name='نام ماده',null=True, blank=True )
    material_color = models.CharField(max_length=50, verbose_name='رنگ',null=True, blank=True )
    material_unit = models.CharField(max_length=20, verbose_name='واحد',null=True, blank=True )
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی', blank=True, null=True)

    objects = models.Manager()
    
    class Meta:
        verbose_name = 'ماده اولیه'
        verbose_name_plural = 'مواد اولیه'

    def __str__(self):
        return self.material_name