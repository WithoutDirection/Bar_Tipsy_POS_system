from django.contrib import admin
from .models import MenuItem, Seat, Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('seat', 'menu_item', 'quantity', 'price', 'status', 'timestamp')

admin.site.register(MenuItem)
admin.site.register(Seat)
admin.site.register(Order, OrderAdmin)
