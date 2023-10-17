'''
۲۰۲۰ Black Users Database Model
'''

# Import all requirements
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.cache import cache
from django.conf import settings
from django.db import models
from django import forms


# Custom User Manager class
class CustomUserManager(BaseUserManager):
    def create_user(self, phoneNumber, password=None, **extra_fields):
        if not phoneNumber:
            raise ValueError('شماره تماس باید وارد شود')
        user = self.model(phoneNumber=phoneNumber, **extra_fields)
        user.set_password(password)
        user.has_new_password = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phoneNumber, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('has_new_password', True)
        return self.create_user(phoneNumber, password, **extra_fields)


class user_accounts(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(db_column='id',primary_key=True, unique=True, verbose_name='شناسه کاربری')
    email = models.CharField(db_column='email',max_length=120, unique=True, null=True, verbose_name='پست الکترونیک')
    username = models.CharField(db_column='username',max_length=120, unique=True, null=True, verbose_name='نام کاربری')
    WPOPass = models.CharField(db_column='WPOPass',max_length=100, default=False, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام خانوادگی')
    phoneNumber = models.CharField(db_column='phoneNumber', max_length=20, unique=True, verbose_name='شماره تماس')
    is_active = models.BooleanField(db_column='is_active',default=True, verbose_name='وضعیت کاربر')
    is_staff = models.BooleanField(db_column='is_staff',default=False, verbose_name='وضعیت راهبری')
    is_supporter = models.BooleanField(blank=True, null=True, verbose_name='عضو تیم پشتیبانی',default=False)
    fadax_payment_possible = models.BooleanField(blank=True, null=True, verbose_name='امکان پرداخت فدکس برای کاربر',default=False)
    date_joined = forms.DateTimeField(
        label='Date Joined',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
    last_login = models.DateTimeField(db_column='last_login',auto_now_add=True, verbose_name='آخرین فعالیت')
    has_new_password = models.BooleanField(db_column='has_new_password',default=True)

    USERNAME_FIELD = 'phoneNumber'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
            return self.phoneNumber
            

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران سایت'


class Customer(models.Model):
    customer = models.CharField(max_length=120, unique=True, null=True, verbose_name='مشتری')
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام خانوادگی')
    code_melli = models.CharField(max_length=100, blank=True, null=True, verbose_name='کد ملی')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='آدرس دقیق')
    static_phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='تلفن ثابت')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='ایمیل')
    pelak = models.CharField(max_length=100, blank=True, null=True, verbose_name='پلاگ\زنگ')
    ostan = models.CharField(max_length=100, blank=True, null=True, verbose_name='استان محل سکونت')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='شهر محل سکونت')
    zip_zode = models.CharField(max_length=100, blank=True, null=True, verbose_name='کد پستی')

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'اطلاعات مشتریان'