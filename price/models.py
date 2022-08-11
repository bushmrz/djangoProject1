from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'цены'
        verbose_name_plural = 'Цены'

class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Заголовок')
    pt_oldPrice = models.CharField(max_length=20, verbose_name='Старая цена')
    pt_newPrice = models.CharField(max_length=20, verbose_name='Новая цена')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'Услуги'