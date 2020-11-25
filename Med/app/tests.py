from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from app.models import *
from app.forms import *

# from app.views import auth

# Create your tests here.

class SIDTest(TestCase):
    def setUp(self) -> None:
        self.symptom = Symptom.objects.create(
                name_symptom= 'Симптом1 1',
                description_symptom= 'Описание')
        self.disease = Disease.objects.create(
                name_disease= 'Заболевание 1',
                description_disease= 'Описание',
                number_of_patients= 2,
                symptoms= self.symptom,
                status_genetic_predisposition= True,
                description_genetic_predisposition='Описание')
        self.patient = Patient.objects.create(
                surname_patient= 'Фамилия',
                name_patient= 'Имя',
                middlename_patient= 'Отчество',
                birthday_patient= '12.10.2009',
                gender_patient= 'Мужской',
                enlightenment_patient= 2,
                number_of_medical_card= 13242342,
                symptoms_patient= self.symptom,
                childhood_diseases= self.disease,
                relatives_diseases= self.disease,
                chronic_disease='Хрон заболевания')
        self.medicalRecord = MedicalRecord.objects.create(
                fk_patient= 'Заболевание 1',
                diseases= self.disease)
    def symptom_in_disease(self):
        self.medicalRecord.fk_patient.add(self.patient)
        self.assertIn(self.patient, self.medicalRecord.fk_patient.all())
        # self.assertEqual(user,account_get)

class TestForms(SimpleTestCase):
    def test_symptom_form_valid_data(self):
        form = SymptomForm(data={
            'name_symptom': 'Наименование',
            'description_symptom': 'Описание'
        })
        self.assertTrue(form.is_valid())

    def test_symptom_form_no_data(self):
        form = SymptomForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)