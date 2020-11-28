from django.db import models
from django.shortcuts import reverse
from django.dispatch import receiver
from account.models import Account

# Create your models here.

# Пациент
class Patient(models.Model):
    surname_patient             = models.CharField(max_length=50, verbose_name='Фамилия пациента', null=True, blank=True)
    name_patient                = models.CharField(max_length=50, verbose_name='Имя пациента', null=True, blank=True)
    middlename_patient          = models.CharField(max_length=50, verbose_name='Отчество пациента', null=True, blank=True)
    email                       = models.EmailField(verbose_name='Почта', max_length=254, null=True, blank=True)
    birthday_patient            = models.DateField(max_length=50, verbose_name='День рождение пациента', null=True, blank=True)
    gender_patient              = models.CharField(max_length=50, verbose_name='Пол пациента', null=True, blank=True)
    enlightenment_patient       = models.CharField(max_length=50, verbose_name='Санитарное просвящение пациента', null=True)
    number_of_medical_card      = models.CharField(max_length=50, verbose_name='Номер медицинской карты', null=True)
    symptoms_patient            = models.ManyToManyField('Symptom', verbose_name="Симптомы", related_name = 'symptoms_patient' , blank=True)
    childhood_diseases          = models.ManyToManyField('Disease', verbose_name="Болезни детства", related_name = 'childhood_diseases', blank=True)
    relatives_diseases          = models.ManyToManyField('Disease', verbose_name="Болезни у родственников", related_name = 'relatives_diseases', blank=True)
    chronic_disease             = models.CharField(max_length=250, verbose_name='Хронические заболевания', null=True, blank=True)
    description_recommendation  = models.CharField(max_length=200, verbose_name='Описание рекомендации', null=True, blank=True)
    date_recommendation         = models.DateField(max_length=50, verbose_name='Дата выдачи рекомендации', null=True, blank=True)
    period_recommendation       = models.DateField(max_length=50, verbose_name='Период времени', null=True, blank=True)
    fk_account                  = models.ForeignKey(Account, on_delete = models.DO_NOTHING, verbose_name = 'Врач', null=True, blank=True)

    class Meta:
        verbose_name            = "Пациент"
        verbose_name_plural     = "Пациенты"

# Указали какая именно будет выводиться информация если мы будем выводить просто объект
    def __str__(self):
        return self.surname_patient + ' ' + self.name_patient + ' ' + self.middlename_patient

    
    def get_absolute_url(self):
        return '/patient'

# Симптом
class Symptom(models.Model):
    name_symptom            = models.CharField(max_length=50, verbose_name='Наименование симптома', null=False)
    description_symptom     = models.CharField(max_length=200, verbose_name='Описание симптома', null=False)
    
    class Meta:
        verbose_name            = "Симптом"
        verbose_name_plural     = "Симптомы"

    def __str__(self):
        return self.name_symptom

    def get_absolute_url(self):
        return '/symptom'

# Заболевание
class Disease(models.Model):
    name_disease                                = models.CharField(max_length=50, verbose_name='Наименование заболевания', null=False)
    description_disease                         = models.TextField(verbose_name='Описание заболевания', null=False)
    number_of_patients                          = models.IntegerField(verbose_name='Количество заболевших', null=True, default=0)
    symptoms                                    = models.ManyToManyField(Symptom, verbose_name="Симптом", related_name='diseases')
    status_genetic_predisposition               = models.BooleanField( verbose_name='Наличие генетических предрасположенностей', default=False)
    description_genetic_predisposition          = models.TextField(verbose_name='Описание генетической предрасположенности', null=True, blank=True, default='-')
    
    class Meta:
        verbose_name            = "Заболевание"
        verbose_name_plural     = "Заболевания"

    def __str__(self):
        return self.name_disease

    def get_absolute_url(self):
        return '/disease'

# Медицинская карта
class MedicalRecord(models.Model):
    fk_patient      = models.ForeignKey(Patient, on_delete = models.DO_NOTHING, verbose_name = 'Пациент', null=False)
    diseases        = models.ManyToManyField(Disease, verbose_name = 'Заболевание', related_name='MedicalRecords')
    
    class Meta:
        verbose_name            = "Медицинская карта"
        verbose_name_plural     = "Медицинские карты"

    def __str__(self):
        return self.fk_patient.surname_patient + ' ' + self.fk_patient.name_patient + ' ' + self.fk_patient.middlename_patient

    def get_absolute_url(self):
        return '/medicalRecord'

class Inform(models.Model):
    email_addres                = models.EmailField(max_length=250, verbose_name='Email пользователя')
    topic                       = models.CharField(max_length=50, verbose_name='Тема сообщения')
    problem_description         = models.TextField(max_length=5000, verbose_name='Описание проблемы')

    class Meta:
        verbose_name            = "Оповещение пациента"
        verbose_name_plural     = "Оповещения пациентов"

    def __str__(self):
        return self.email_addres


