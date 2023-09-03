from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from firstapp.views import homeView
from rest_framework.authtoken.views import obtain_auth_token
from students import views
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/firstapp/', include('firstapp.urls')),
    path('', homeView),
    path('api/login-api/', obtain_auth_token),
    path('api/token/', MyTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # From Study Mart DRF Tutorial
    path('students/', views.student_info),
    path('students/<int:pk>', views.student_instance),
    path('aicreate', views.students_create, name='studentcreate'),    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

