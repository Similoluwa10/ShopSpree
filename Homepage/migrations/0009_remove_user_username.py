# Generated by Django 5.1.1 on 2024-11-29 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0008_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
