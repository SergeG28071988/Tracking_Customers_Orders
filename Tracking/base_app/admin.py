from django.contrib import admin
from .models import *
from django.utils.html import format_html, mark_safe

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_photo')
    fields = ['name', 'email', ('phone', 'photo', 'show_photo')]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        if obj.photo:
            return format_html(
                f'<img src="{obj.photo.url}" style="max-height: 100px;">')
            # можно и с использованием функции mark_safe
            # return mark_safe(
            # f'<img src="{obj.photo.url}" style="max-height: 100px;">')
        else:
            return "Фото не доступно"

    show_photo.short_description = 'Фото клиента'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', 'product', 'category', 'show_photo', 'order_date',
                    'order_amount', 'status', 'completed')
    list_filter = ('order_number', 'client')    
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        if obj.photo:
            return format_html(
                f'<img src="{obj.photo.url}" style="max-height: 100px;">')
            # можно и с использованием функции mark_safe
            # return mark_safe(
            # f'<img src="{obj.photo.url}" style="max-height: 100px;">')
        else:
            return "Фото не доступно"

    show_photo.short_description = 'Фото товара'    