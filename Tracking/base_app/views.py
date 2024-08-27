from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('index')

# Общий маршрут
def index(request):
    context = {
        'title': 'Главная страница сайта'
    }
    return render(request, 'index.html', context)

# Функции для работы с клиентами
def client_list(request):
    return render(request, 'client_list.html')

def display_clients(request):
    clients = Client.objects.all()

    context = {
        'clients': clients,
        'header': 'Клиенты'
    }

    return render(request, 'client_list.html', context)

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
        context = {
            'form': form,
            'header': 'Добавить клиента '
        }
        return render(request, 'add_client.html', context)

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    context = {
        'client': client,
    }

    return render(request, 'client_detail.html', context)

def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_list")

    else:
        form = ClientForm(instance=client)
        context = {
            'form': form,
            'header': 'Редактировать клиента',
        }

        return render(request, 'edit_client.html', context)
    
def delete_client(request, pk):
    clients = get_object_or_404(Client, pk=pk)
    clients.delete()
    return redirect("client_list")

def search_clients(request):
    name = request.GET.get('name')
    clients = Client.objects.filter(name__icontains=name)
    header = f"Найден клиент '{name}'"
    context = {
        'clients': clients,
        'header': header
    }
    return render(request, 'client_list.html', context)

def print_clients(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

# Функции для работы с заказами
def plot_order_statistics(orders):
    fig, ax = plt.subplots()

    order_date = [order.order_date for order in orders]
    order_amounts = [order.order_amount for order in orders]

    ax.bar(order_date, order_amounts, color='skyblue')
    plt.xlabel('Дата заказа')
    plt.ylabel('Сумма заказа')
    plt.title('Статистика заказов')
    plt.xticks(rotation=45)

    graph_file = BytesIO()
    plt.savefig(graph_file, format='png')
    graph_file.seek(0)

    graph_base64 = base64.b64encode(graph_file.read()).decode()

    plt.close('all')

    return graph_base64

def order_list(request):
    return render(request, 'order_list.html')

def display_orders(request):
    orders = Order.objects.all()
    graph_base64 = plot_order_statistics(orders)

    context = {
        'orders': orders,
        'graph_base64': graph_base64,
        'header': 'Заказы'
    }
    return render(request, 'order_list.html', context)

def add_order(request): 
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
        context = {
            'form': form,
            'header': 'Добавить заказ '
        }
        return render(request, 'add_order.html', context)

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    context = {
        'order': order,
    }

    return render(request, 'order_detail.html', context)

def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_list")

    else:
        form = OrderForm(instance=order)
        context = {
            'form': form,
            'header': 'Редактировать заказ',
        }

        return render(request, 'edit_order.html', context)
    
def delete_order(request, pk):
    orders = get_object_or_404(Order, pk=pk)
    orders.delete()
    return redirect("order_list")    

def search_orders(request):
    client = request.GET.get('client')
    if client:
        orders = Order.objects.filter(client__name__icontains=client)
        header = f"Search results for '{client}'"
    else:
        orders = Order.objects.all()
        header = "All Orders"

    graph_base64 = plot_order_statistics(orders)

    context = {
        'orders': orders,
        'header': header,
        'graph_base64': graph_base64,
    }
    return render(request, 'order_list.html', context)

def print_orders(request): 
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
