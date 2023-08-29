# DJango Rest Framwork Learning
 
## Create Virtual Enviroment and activate it:
python -m venv venv
venv/Scripts/activate

## Install Django & Django Framework
pip install django djangorestframework

## Create a project
django-admin startproject myproject 

## Create an app
python manage.py startapp firstapp

## Add the following line on settings.py for apps static and media folder.

INSTALLED_APPS = [
'rest_framework',
'firstapp'
]

TEMPLATES = [
{
'DIRS': ['templates'],
},
]

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



## Add following line on on project urls.py

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

