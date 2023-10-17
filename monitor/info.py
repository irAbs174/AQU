from django.urls import re_path
from .usage import uptime, memusage, cpuusage, getdisk, getusers, getips, gettraffic, getproc, getdiskio, loadaverage, platform, getcpus, getnetstat


urlpatterns = [
    re_path(r'uptime/$', uptime, name='uptime'),
    re_path(r'memory/$', memusage, name='memusage'),
    re_path(r'cpuusage/$', cpuusage, name='cpuusage'),
    re_path(r'getdisk/$', getdisk, name='getdisk'),
    re_path(r'getusers/$', getusers, name='getusers'),
    re_path(r'getips/$', getips, name='getips'),
    re_path(r'gettraffic/$', gettraffic, name='gettraffic'),
    re_path(r'proc/$', getproc, name='getproc'),
    re_path(r'getdiskio/$', getdiskio, name='getdiskio'),
    re_path(r'loadaverage/$', loadaverage, name='loadaverage'),
    re_path(r'platform/([\w\-\.]+)/$', platform, name='platform'),
    re_path(r'getcpus/([\w\-\.]+)/$', getcpus, name='getcpus'),
    re_path(r'getnetstat/$', getnetstat, name='getnetstat'),
]