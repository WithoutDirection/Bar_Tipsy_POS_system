# Create your models here.
from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=30, help_text='品項名稱')
    price = models.IntegerField(help_text='價格')

    def __str__(self):
        return self.name
# Create your models here.

class Seat(models.Model):
    name = models.CharField(max_length=30, help_text='座位')
    

    def __str__(self):
        return self.name

class Order(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='品項')
    quantity = models.IntegerField(help_text='數量')
    timestamp = models.DateTimeField(auto_now_add=True, help_text='時間戳記')
    status = models.BooleanField(default=False, help_text='已出單')
    

    def __str__(self):
        return self.menu_item.name
    
    @property
    def price (self):
        return self.menu_item.price * self.quantity