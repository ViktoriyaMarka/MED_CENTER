# Generated by Django 3.1.2 on 2020-11-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_inform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inform',
            name='email_addres',
            field=models.EmailField(max_length=250, verbose_name='Email пользователя'),
        ),
    ]
