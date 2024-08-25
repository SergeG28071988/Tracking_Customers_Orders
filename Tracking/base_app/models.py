from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Client(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    photo = models.ImageField(upload_to='images',
                              help_text="Введите фото",
                              verbose_name="Фото клиента",
                              null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    objects = None
    order_number = models.CharField(max_length=100, verbose_name='Номер заказа')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент')
    product = models.CharField(max_length=100, verbose_name="Товар")
    CATEGORY_CHOICES = [
        ('Процессоры', 'Процессоры'),
        ('Материнские платы', 'Материнские платы'),
        ('Видеокарты', 'Видеокарты'),
        ('Оперативная память', 'Оперативная память'),
        ('SSD-диски', 'SSD-диски'),
        ('HDD-диски', 'HDD-диски'),
        ('Блоки питания>', 'Блоки питания'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='Категория')
    photo = models.ImageField(upload_to='images',
                              help_text="Введите фото",
                              verbose_name="Фото товара",
                              null=True, blank=True)
    
    order_date = models.DateField(verbose_name='Дата заказа')
    order_amount = models.DecimalField(verbose_name="Сумма заказа", max_digits=10, decimal_places=2)
    ORDER_STATUS_CHOICES = [
        ('Поступил', 'Поступил'),
        ('Выполняется', 'Выполняется'),
        ('Закрыт', 'Закрыт'),
    ]
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, verbose_name='Статус')
    completed = models.BooleanField(default=False, verbose_name='Заказ завершен')
    completion_date = models.DateField(null=True, blank=True, verbose_name='Дата завершения')


    def __str__(self):
        return f'{self.order_number} {self.client}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


@receiver(pre_save, sender=Order)
def update_completion_date(sender, instance, **kwargs):
    if instance.completed and not instance.completion_date:
        instance.completion_date = instance.date_created