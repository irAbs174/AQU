from django.db import models

class Units(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام واحد', blank=True, null=True)
    symbol = models.CharField(max_length=20, verbose_name='نماد واحد', blank=True, null=True)
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی', blank=True, null=True)

    class Meta:
        verbose_name = 'واحد اندازه گیری'
        verbose_name_plural = 'واحد های اندازه گیری'

    def __str__(self):
        return self.name
