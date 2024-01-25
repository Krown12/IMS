# Generated by Django 5.0.1 on 2024-01-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Electronics', 'E'), ('Clothing', 'C'), ('Home and Kitchen', 'HK'), ('Books', 'B'), ('Sports and Outdoors', 'S&O'), ('Beauty and Personal Care', 'B&PC'), ('Toys and Games', 'T&G'), ('Furniture', 'F'), ('Automotive', 'A'), ('Health and Wellness', 'H&W'), ('Grocery', 'G'), ('Jewelry', 'J')], default='NONE', max_length=100),
        ),
    ]
