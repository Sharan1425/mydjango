from django.contrib import admin
from django.urls import path
from .  import views

urlpatterns = [
    path('register/', views.registerpage, name = 'registerpage'),
    path('login/', views.login_page, name = 'login_page'),
    path('logout/', views.logout_page, name = 'logout_page'),
    path('', views.home,name = 'home'),
    path('products/', views.products, name = 'products'),
    #path('customers/', views.customers, name = 'customers'),
    path('customers/<str:pk_test>/', views.customers, name = 'customers'),
    path('createorder/', views.createorder, name = 'createorder'),
    path('updateorder/<str:pk>/', views.updateorder, name = 'updateorder'),
    path('deleteorder/<str:pk>/', views.deleteorder, name = 'deleteorder'),
    
] 