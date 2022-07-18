from django.db import models

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name= 'Дата')
    order_name = models.CharField(max_length=100, verbose_name= 'Имя')
    order_phone = models.CharField(max_length=10, verbose_name= 'Номер телефона')

    def __str__(self):
        return  self.order_name

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
