# Generated by Django 4.1.12 on 2023-12-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_key', models.CharField(blank=True, max_length=50, null=True, verbose_name='کلید')),
                ('rate_author', models.CharField(blank=True, max_length=40, null=True, verbose_name='ثبت کننده نرخ')),
                ('rate_value', models.FloatField(blank=True, null=True, verbose_name='نرخ')),
                ('rate_unit', models.CharField(blank=True, max_length=40, null=True, verbose_name='واحد نرخ')),
                ('rate_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ و زمان نرخ گذاری')),
            ],
            options={
                'verbose_name': 'نرخ تولید',
                'verbose_name_plural': 'نرخ های تولید',
            },
        ),
    ]