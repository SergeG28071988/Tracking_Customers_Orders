from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage
from .views import logout_view

urlpatterns = [
    # Маршруты для входа на сайт / в приложение
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    # Маршрут общий
    path('', views.index, name='index'),  # общий маршрут
    
    # Маршруты для работы с клиентами
    path('client_list/', views.client_list, name='client_list'), # список клиентов
    path('display_clients/', views.display_clients, name='display_clients'), # вывод клиентов
    path('add_client/', views.add_client, name='add_client'), # добавление клиентов
    path('client/<int:pk>/', views.client_detail, name='client_detail'), # информация о клиентах
    path('edit_client/<int:pk>/', views.edit_client, name='edit_client'), # редактирование клиента
    path('delete_client/<int:pk>/', views.delete_client, name='delete_client'), # удаление клиента
    path('search_clients/', views.search_clients, name='search_clients'), # поиск клиента
    path('print_clients/', views.print_clients, name='print_clients'), # печать списка клиентов
    
    # Маршруты для работы с заказами
    path('order_list/', views.order_list, name='order_list'), # список заказов    
    path('display_orders/', views.display_orders, name='display_orders'), # вывод заказов
    path('add_order/', views.add_order, name='add_order'), # добавление заказов
    path('order/<int:pk>/', views.order_detail, name='order_detail'), # информация о заказе
    path('edit_order/<int:pk>/', views.edit_order, name='edit_order'), # редактирование заказа
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'), # удаление клиента
    path('search_orders/', views.search_orders, name='search_orders'), # поиск заказов по клиенту
    path('print_orders/', views.print_orders, name='print_orders'), # печать списка заказов
]
