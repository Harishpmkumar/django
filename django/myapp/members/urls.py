from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('index/', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
]
