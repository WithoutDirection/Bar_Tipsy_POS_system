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
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menu_item')
    quantity = models.IntegerField(help_text='數量')
    timestamp = models.DateTimeField(auto_now_add=True, help_text='時間戳記')
    status = models.CharField(max_length=10, help_text='狀態')
    price = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='price')

    def __str__(self):
        return self.menu_item.name