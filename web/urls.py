"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 

from core.views import *

urlpatterns = [
    path('', main, name='main'),
    path('download/', one_python_download, name='first'),
    path('idle/', two_idle_program, name='second'),
    path('syntax/', three_python_syntax, name='third'),
    path('if_else/', four_if_else, name='fourth'),
    path('loops/', five_loops, name='fifth'),
    path('keywords/', six_keywords, name='sixth'),
    path('functions/', seven_functions, name='seventh'),
    path('numbers/', eight_numbers, name='eighth'),
    path('lists/', nine_lists, name='nineth'),
    path('indexes/', ten_indexes, name='tenth'),
    path('tuples/', eleven_tuples, name='eleventh'),
    path('dicts/', twelve_dicts, name='twelveth'),
    path('sets/', thirteen_sets, name='thirteenth'),
    path('def/', fourteen_def, name='fourteenth'),
    path('os/', fifteen_os, name='fifteenth'),
    path('404/', error404, name='404'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
