from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select, SelectMultiple, Textarea, CheckboxInput, NumberInput, EmailInput, FileInput
from account.models import Account
from app.models import *

class AccountForm(ModelForm):
    class Meta: 
        model = Account
        fields = ['username', 'password', 'surname_doctor', 'name_doctor', 'middlename_doctor', 'positions_doctor']

        widgets = {
            "positions_doctor": Select(attrs={
                'class': 'input_text'
            })
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class InformForm(ModelForm):
    class Meta:
        model = Inform
        fields = '__all__'

        widgets = {
            "email_addres": TextInput(attrs={
                'class': 'input_text'
            }),

            "topic": TextInput(attrs={
                'class': 'input_text'
            }),

            "problem_description": Textarea(attrs={
                'class': 'input_text report'
            })
        }

class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = ['name_disease', 'description_disease', 'symptoms', 'status_genetic_predisposition', 'description_genetic_predisposition']

        widgets = {
            "symptoms": SelectMultiple(attrs={
                'class': 'input_text symptoms',
                'required': 'true'
            }),

            "name_disease": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "description_disease": Textarea(attrs={
                'class': 'input_text disease',
                'required': 'true'
            }),

            "description_genetic_predisposition": Textarea(attrs={
                'class': 'input_text disease',
                'required': 'true'
            })
        }

class SymptomForm(ModelForm):
    class Meta:
        model = Symptom
        fields = '__all__'

        widgets = {
            "name_symptom": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "description_symptom": Textarea(attrs={
                'class': 'input_text symptom',
                'required': 'true'
            })
        }

class MedicalRecordForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['surname_patient','name_patient','middlename_patient','symptoms_patient','number_of_medical_card']

        widgets = {
            "surname_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "name_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "middlename_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "symptoms_patient": SelectMultiple(attrs={
                'class': 'input_text patient',
                'required': 'true'
            }),

            "number_of_medical_card": NumberInput(attrs={
                'class': 'input_text',
                'required': 'true'
            })
        }


class RecommendationForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        widgets = {
            "date_recommendation": DateInput(attrs={
                'class': 'input_text',
                'type' : 'date',
                'required': 'true'
            }),

            "period_recommendation": DateInput(attrs={
                'class': 'input_text',
                'type' : 'date',
                'required': 'true'
            }),

            "email": EmailInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "description_recommendation": Textarea(attrs={
                'class': 'input_text recommendation',
                'required': 'true'
            }),

            "fk_account": Select(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "surname_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "name_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "middlename_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "birthday_patient": DateInput(attrs={
                'class': 'input_text',
                'type' : 'date',
                'required': 'true'
            }),

            "number_of_medical_card": NumberInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "gender_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "enlightenment_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "symptoms_patient": SelectMultiple(attrs={
                'class': 'input_text patient',
                'required': 'true'
            }),

            "childhood_diseases": SelectMultiple(attrs={
                'class': 'input_text patient',
                'required': 'true'
            }),

            "relatives_diseases": SelectMultiple(attrs={
                'class': 'input_text patient',
                'required': 'true'
            }),

            "chronic_disease": Textarea(attrs={
                'class': 'input_text disease',
                'required': 'false'
            })
        }


# ПАЦИЕНТ -------------------------------------------------------


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['surname_patient', 'name_patient', 'middlename_patient', 'number_of_medical_card', 'symptoms_patient', 'childhood_diseases', 'relatives_diseases', 'chronic_disease','gender_patient','enlightenment_patient','birthday_patient','email']

        widgets = {
            "email": EmailInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "surname_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "name_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "middlename_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            " ": DateInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "number_of_medical_card": NumberInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "gender_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "enlightenment_patient": TextInput(attrs={
                'class': 'input_text',
                'required': 'true'
            }),

            "symptoms_patient": SelectMultiple(attrs={
                'class': 'input_text patient',
                'required': 'true'
            }),

            "childhood_diseases": SelectMultiple(attrs={
                'class': 'input_text patient',
                'required': 'true'
            }),

            "relatives_diseases": SelectMultiple(attrs={
                'class': 'input_text patient',
                'required': 'true'
            }),

            "chronic_disease": TextInput(attrs={
                'class': 'input_text disease',
                'required': 'false'
            })
        }

