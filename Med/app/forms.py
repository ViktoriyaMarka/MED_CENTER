from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select, SelectMultiple, Textarea, CheckboxInput, NumberInput
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

class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = ['name_disease', 'description_disease', 'symptoms', 'status_genetic_predisposition', 'description_genetic_predisposition']

        widgets = {
            "symptoms": SelectMultiple(attrs={
                'class': 'input_text symptoms'
            }),

            "name_disease": TextInput(attrs={
            'class': 'input_text'
            }),

            "description_disease": Textarea(attrs={
            'class': 'input_text disease',
            }),

            "description_genetic_predisposition": Textarea(attrs={
            'class': 'input_text disease'
            })
        }

# class DistributionForm(ModelForm):
#     class Meta:
#         model = Distribution
#         fields = '__all__'

#         widgets = {
#             "name_distribution": TextInput(attrs={
#             'class': 'input_text'
#             }),

#             "fk_patient": Select(attrs={
#             'class': 'input_text'
#             }),

#             "fk_doctor": Select(attrs={
#             'class': 'input_text'
#             })
#         }

class SymptomForm(ModelForm):
    class Meta:
        model = Symptom
        fields = '__all__'

        widgets = {
            "name_symptom": TextInput(attrs={
            'class': 'input_text'
            }),

            "description_symptom": Textarea(attrs={
            'class': 'input_text symptom'
            })
        }

class MedicalRecordForm(ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

        widgets = {
            "fk_patient": Select(attrs={
            'class': 'input_text'
            }),

            "diseases": SelectMultiple(attrs={
            'class': 'input_text symptom'
            })
        }


class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = '__all__'

        widgets = {
            "description_recommendation": Textarea(attrs={
            'class': 'input_text recommendation'
            }),

            "fk_distribution": Select(attrs={
            'class': 'input_text',
            })
        }

# ПАЦИЕНТ -------------------------------------------------------


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields ='__all__'

        widgets = {
            "surname_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "name_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "middlename_patient": TextInput(attrs={
                'class': 'input_text',
            }),

            "number_of_medical_card": NumberInput(attrs={
                'class': 'input_text',
            }),

            "symptoms_patient": SelectMultiple(attrs={
                'class': 'input_text process'
            }),

            "childhood_diseases": SelectMultiple(attrs={
                'class': 'input_text process'
            }),

            "relatives_diseases": SelectMultiple(attrs={
                'class': 'input_text process'
            }),

            "chronic_disease": Textarea(attrs={
            'class': 'input_text process bigest',
            })
        }

