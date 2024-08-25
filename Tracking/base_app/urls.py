from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage
from .views import logout_view

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    # Маршруты
    path('', views.index, name='index'),  # общий маршрут
    path('client_list/', views.client_list, name='client_list'),
    path('display_clients/', views.display_clients, name='display_clients'),
    path('add_client/', views.add_client, name='add_client'),
    path('client/<int:pk>/', views.client_detail, name='client_detail'),

    path('order_list/', views.order_list, name='order_list'),
]
