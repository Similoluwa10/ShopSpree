# Generated by Django 5.1.1 on 2024-11-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0009_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]