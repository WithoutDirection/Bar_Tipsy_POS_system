# Generated by Django 5.0.1 on 2024-01-29 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='品項名稱', max_length=30)),
                ('price', models.IntegerField(help_text='價格')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='座位', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='數量')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='時間戳記')),
                ('status', models.CharField(help_text='狀態', max_length=10)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='order_sys.menuitem')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_sys.seat')),
            ],
        ),
    ]