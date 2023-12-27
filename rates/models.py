from django.db import models

class Rates(models.Model):
    rate_key = models.CharField(max_length=50, verbose_name='کلید', null=True, blank=True)
    rate_author = models.CharField(max_length=40, verbose_name='ثبت کننده نرخ', null=True, blank=True)
    rate_value = models.FloatField(verbose_name='نرخ', blank=True, null=True)
    rate_unit = models.CharField(max_length=40, verbose_name='واحد نرخ', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی', blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'نرخ تولید'
        verbose_name_plural = 'نرخ های تولید'

    def __str__(self):
        return f"({self.rate_key})=>({self.rate_author}=>{self.rate_value})"