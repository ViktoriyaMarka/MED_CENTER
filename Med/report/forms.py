from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select, SelectMultiple, Textarea, CheckboxInput, FileInput
from report.models import *

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

        widgets = {
            "type_errors": Select(attrs={
                'class': 'input_text'
            }),

            "topic": TextInput(attrs={
                'class': 'input_text'
            }),

            "problem_description": Textarea(attrs={
                'class': 'input_text report'
            }),

            "image": FileInput(attrs={
            })
        }