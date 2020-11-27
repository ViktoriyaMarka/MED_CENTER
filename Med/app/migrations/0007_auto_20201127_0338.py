# Generated by Django 3.1.2 on 2020-11-27 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201127_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inform',
            name='file_inform',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
    ]
