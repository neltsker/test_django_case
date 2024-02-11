from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField('name of menu', max_length=30, unique=True)
    description = models.TextField('desc of menu', max_length=300, blank=True)
    
    class Meta:
        ordering=['id']
        verbose_name='Меню'
        verbose_name_plural='Меню'

    def __str__(self):
        return self.name
    


class MenuItem(models.Model):
    name = models.CharField('name of Item', max_length=50, unique=True)
    description = models.TextField('desc of item', max_length=300, blank=True)

    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True)
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='MenuItems')

    class Meta:
        ordering=['id']
        verbose_name='пункт меню'
        verbose_name_plural = 'пункт меню'

    def __str__(self):
        return self.name