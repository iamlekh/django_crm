
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name = "home"),
    path('products/', views.products , name = "products"),
    path('register/', views.registerPage , name = "register"),
    path('login/', views.loginPage , name = "login"), 
    path('logout/', views.logoutUser , name = "logout"),
    path('user/', views.userPage, name="user-page"), 
    path('customer/<str:pk>/', views.customer , name = "customer"),
    path('creat_order/<str:pk>/', views.createOrder, name = 'creat_order'),
    path('update_order/<str:pk>/', views.updateOrder, name = 'update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name = 'delete_order'),
]
