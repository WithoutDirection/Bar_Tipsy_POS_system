# Generated by Django 5.0.1 on 2024-01-29 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_sys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AlterField(
            model_name='order',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='品項', to='order_sys.menuitem'),
        ),
    ]
