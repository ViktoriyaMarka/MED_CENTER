from django.db import models
from django.shortcuts import reverse
from django.dispatch import receiver
from account.models import Account

# Create your models here.


# Распределение
# class Distribution(models.Model):
#     name_distribution   = models.CharField(max_length=50, verbose_name='Наименование распределения', default="")
#     fk_patient          = models.ForeignKey(Patient, on_delete = models.DO_NOTHING, verbose_name = 'Пациент', null=True)
#     fk_doctor           = models.ForeignKey(Account, on_delete = models.DO_NOTHING, verbose_name = 'Врач', null=True)
    
#     class Meta:
#         verbose_name = "Пациент и Врач"
#         verbose_name_plural = "Распределения пациентов"
#     def __str__(self):
#         return self.fk_patient.surname_patient + ' ' + self.fk_patient.name_patient + ' ' + self.fk_patient.middlename_patient + ' : ' + self.fk_doctor.surname_doctor + ' ' + self.fk_doctor.name_doctor + ' ' + self.fk_doctor.middlename_doctor

#     def get_absolute_url(self):
#         return '/distribution'

# Пациент
class Patient(models.Model):
    surname_patient             = models.CharField(max_length=50, verbose_name='Фамилия пациента')
    name_patient                = models.CharField(max_length=50, verbose_name='Имя пациента')
    middlename_patient          = models.CharField(max_length=50, verbose_name='Отчество пациента')
    birthday_patient            = models.DateField(max_length=50, verbose_name='День рождение пациента')
    gender_patient              = models.CharField(max_length=50, verbose_name='Пол пациента')
    enlightenment_patient       = models.CharField(max_length=50, verbose_name='Санитарное просвящение пациента')
    number_of_medical_card      = models.CharField(max_length=50, verbose_name='Номер медицинской карты', null=False)
    symptoms_patient            = models.ManyToManyField('Symptom', verbose_name="Симптомы", related_name = 'symptoms_patient' , blank=True)
    childhood_diseases          = models.ManyToManyField('Disease', verbose_name="Болезни детства", related_name = 'childhood_diseases', blank=True)
    relatives_diseases          = models.ManyToManyField('Disease', verbose_name="Болезни у родственников", related_name = 'relatives_diseases', blank=True)
    chronic_disease             = models.CharField(max_length=250, verbose_name='Хронические заболевания', null=True)

    class Meta:
        verbose_name            = "Пациент"
        verbose_name_plural     = "Пациенты"

# Указали какая именно будет выводиться информация если мы будем выводить просто объект
    def __str__(self):
        return self.surname_patient + ' ' + self.name_patient + ' ' + self.middlename_patient

    # def get_absolute_url(self):
    #     return reverse("process", kwargs={"pk": self.pk})

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



# Рекомендация
class Recommendation(models.Model):
    description_recommendation      = models.CharField(max_length=200, verbose_name='Описание рекомендации')
    date_recommendation             = models.DateField(max_length=50, verbose_name='Дата выдачи рекомендации')
    period_recommendation           = models.DateField( verbose_name='Период времени')
    fk_distribution                 = models.ForeignKey(Account, on_delete = models.DO_NOTHING, verbose_name = 'Врач', null=False)

    class Meta:
        verbose_name            = "Рекомендация"
        verbose_name_plural     = "Рекомендации"

    def __str__(self):
        # return self.fk_distribution.fk_patient.name_patient + ' ' + self.fk_distribution.fk_patient.surname_patient + ' ' + self.fk_distribution.fk_patient.middlename_patient + ' : ' + self.fk_distribution.fk_doctor.name_doctor + ' ' + self.fk_distribution.fk_doctor.surname_doctor + ' ' + self.fk_distribution.fk_doctor.middlename_doctor
        return self.description_recommendation
    
    def get_absolute_url(self):
        return '/recommendation'



