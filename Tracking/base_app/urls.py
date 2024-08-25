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
    # Маршруты для работы с клиентами
    path('client_list/', views.client_list, name='client_list'), # список клиентов
    path('display_clients/', views.display_clients, name='display_clients'),
    path('add_client/', views.add_client, name='add_client'), # добавление клиентов
    path('client/<int:pk>/', views.client_detail, name='client_detail'), # информация о клиентах
    path('edit_client/<int:pk>/', views.edit_client, name='edit_client'), # редактирование клиента
    path('delete_client/<int:pk>/', views.delete_client, name='delete_client'), # удаление клиента
    path('search_clients/', views.search_clients, name='search_clients'), # поиск клиента
    path('print_clients/', views.print_clients, name='print_clients'), # печать списка клиентов
    # Маршруты для работы с заказами
    path('order_list/', views.order_list, name='order_list'), # список заказов
]
