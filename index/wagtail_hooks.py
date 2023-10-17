from .views import visit_view, mounth_visit_view, week_visit_view, daily_visit_view
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from django.urls import path, reverse
from wagtail import hooks


@hooks.register('register_admin_urls')
def register_daily_visit():
    return [
        path('visit', visit_view, name='visits'),
        path('visit/mounth', mounth_visit_view, name='mounth_visits'),
        path('visit/week', week_visit_view, name='week_visits'),
        path('visit/daily', daily_visit_view, name='daily_visits'),
    ]

@hooks.register('register_admin_menu_item')
def register_daily_visit_item():
    submenu = Menu(items=[
        MenuItem('بازدید کلی', reverse('visits'), icon_name='clipboard-list'),
        MenuItem('بازدید ماه جاری', reverse('mounth_visits'), icon_name='calendar-alt'),
        MenuItem('بازدید هفته جاری', reverse('week_visits'), icon_name='calendar-check'),
        MenuItem('بازدید امروز', reverse('daily_visits'), icon_name='view'),
    ])

    return SubmenuMenuItem('آمار سایت', submenu, icon_name='pick')