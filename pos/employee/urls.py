from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('about-page/', views.about, name='about'),
    
]
