# Generated by Django 4.2.1 on 2023-06-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True, verbose_name='کاربر')),
                ('operator', models.CharField(blank=True, max_length=100, null=True, verbose_name='پشتیبان')),
                ('request_submit', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ثبت درخواست')),
                ('support_request', models.CharField(blank=True, max_length=100, null=True, verbose_name='درخواست پشتیبانی')),
            ],
            options={
                'verbose_name': 'درخواست پشتیبانی',
                'verbose_name_plural': 'درخواست های پشتیبانی',
            },
        ),
        migrations.AlterModelOptions(
            name='support',
            options={'verbose_name': 'تاریخچه پیام پشتیبانی', 'verbose_name_plural': 'تاریخچه پیام های پشتیبانی'},
        ),
    ]