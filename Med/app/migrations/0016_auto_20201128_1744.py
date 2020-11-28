# Generated by Django 3.1.2 on 2020-11-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20201128_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='childhood_diseases',
            field=models.ManyToManyField(related_name='childhood_diseases', to='app.Disease', verbose_name='Болезни детства'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='relatives_diseases',
            field=models.ManyToManyField(related_name='relatives_diseases', to='app.Disease', verbose_name='Болезни у родственников'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms_patient',
            field=models.ManyToManyField(related_name='symptoms_patient', to='app.Symptom', verbose_name='Симптомы'),
        ),
    ]
