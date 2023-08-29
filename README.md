# DJango Rest Framwork Learning
 
## Create Virtual Enviroment and activate it:
_ _ python -m venv venv
_ _ venv/Scripts/activate

## Install Django & Django Framework
_ _ pip install django djangorestframework

## Create a project
_ _ django-admin startproject myproject 

## Create an app
_ _ python manage.py startapp firstapp

## Add the following line on settings.py for apps static and media folder.

_ _ INSTALLED_APPS = [
_ _     'rest_framework',
_ _     'firstapp'
_ _ ]

_ _ TEMPLATES = [
_ _     {
_ _         'DIRS': ['templates'],
_ _     },
_ _ ]

_ _ STATIC_URL = '/static/'
_ _ STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

_ _ MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
_ _ MEDIA_URL = '/media/'



## Add following line on on project urls.py

_ _ from django.urls import path, include
_ _ from django.conf import settings
_ _ from django.conf.urls.static import static
_ _ from django.contrib import admin

_ _ urlpatterns = [
_ _     path('admin/', admin.site.urls),
_ _     path('api/', include('rest_framework.urls')),
_ _ ]

_ _ urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
_ _ urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

