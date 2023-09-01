from django.urls import path
from firstapp.views import ContactAPIView
from .views import *

urlpatterns = [
    path('first/', firstAPI),
    path('registration/', registrationAPI),
    path('contact/', ContactAPIView.as_view()),
]
