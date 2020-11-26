from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.contrib.auth import authenticate, login
from account.models import *
from app.models import *
from app.forms import *
from django.views.generic.base import RedirectView
from django.views.generic import View, DeleteView, DetailView, UpdateView
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.

# ДОКТОР
def auth(request):
    return render(request, 'app/login.html')

def register(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            account = authenticate(username=username, password=password)
            login(request, account)
            return redirect ('/accounts/login/')
        else:
            context = {'form': form}
    else:
        form = AccountForm()
        context = {'form': form}
    return render(request, 'registration/reg.html', context)

def profile(request):
    user_id = request.user.id
    user = request.user
    if not user.is_authenticated:
        return redirect('/accounts/login/')

    search_query = request.GET.get('search','')
    if search_query:
        # .objects.select_related().all()
        info = Account.objects.filter(Q(patients__surname_patient__icontains=search_query) | 
        Q(patients__name_patient__icontains=search_query) | 
        Q(patients__middlename_patient__icontains=search_query) |
        Q(patients__gender_patient__icontains=search_query))
    else:
        info = Account.objects.get(pk=request.user.id)
    elements = Disease.objects.all()
    context = {'elements': elements, 'info': info}
    return render(request, 'app/doctor/profile.html', context)


#------------------------------------------------------- Справочники -------------------------------------------------------


# Заболевания -------------------------------------------------------

# Добавление и поиск
def disease(request):
    error = ''
    search_query = request.GET.get('search','')
    if search_query:
        elements = Disease.objects.filter(Q(name_disease__icontains=search_query) | 
        Q(description_disease__icontains=search_query) |
        Q(symptoms__name_symptom__icontains=search_query) |
        Q(description_genetic_predisposition__icontains=search_query))
    else:
        elements = Disease.objects.all()

    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Возникла ошибка'

    form = DiseaseForm()
    context = {'elements': elements, 'form': form}
    return render(request, 'app/doctor/Disease.html', context)

# Изменение
class diseaseUpdateView(View):

    def get(self, request, id):
        disease = Disease.objects.get(pk=id)
        elements = Disease.objects.all()
        disease_form = DiseaseForm(instance = disease)
        return render(request, 'app/doctor/Disease.html', context = {'form': disease_form, 'data': disease, 'elements': elements} )

    def post(self, request, id):
        disease = Disease.objects.get(pk=id)
        disease_form = DiseaseForm(request.POST, instance = disease)

        if disease_form.is_valid():
            disease_form.save()
            return redirect(disease)

        disease_form = DiseaseForm()
        return render(request, 'app/doctor/Disease.html', context = {'form': disease_form, 'data': disease} )
        
# Удаление
class diseaseDeleteView(DeleteView):
    model = Disease
    success_url = '/disease'
    template_name = 'app/doctor/DELETE.html'

# Симптом -------------------------------------------------------
def symptom(request):
    error = ''
    search_query = request.GET.get('search','')
    if search_query:
        elements = Symptom.objects.filter(Q(name_symptom__icontains=search_query) | 
        Q(description_symptom__icontains=search_query))
    else:
        elements = Symptom.objects.all()
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Возникла ошибка'
    form = SymptomForm()
    context = {'elements': elements, 'form': form}
    return render(request, 'app/doctor/Symptom.html', context)

class symptomUpdateView(View):

    def get(self, request, id):
        symptom = Symptom.objects.get(pk=id)
        elements = Symptom.objects.all()
        form = SymptomForm(instance = symptom)
        return render(request, 'app/doctor/Symptom.html', context = {'form': form, 'data':symptom, 'elements': elements} )

    def post(self, request, id):
        symptom = Symptom.objects.get(pk=id)
        form = SymptomForm(request.POST, instance = symptom)
        if form.is_valid():
            form.save()
            return redirect(symptom)
        form = SymptomForm()
        return render(request, 'app/doctor/Symptom.html', context = {'form': form, 'data': symptom} )

# Удаление
class symptomDeleteView(DeleteView):
    model = Symptom
    success_url = '/symptom'
    template_name = 'app/doctor/DELETE.html'

# Медицинские карты -------------------------------------------------------
def medicalRecord(request):
    error = ''
    search_query = request.GET.get('search','')
    if search_query:
        elements = MedicalRecord.objects.filter(Q(fk_patient__surname_patient__icontains=search_query) |
        Q(fk_patient__name_patient__icontains=search_query) |
        Q(fk_patient__middlename_patient__icontains=search_query) | 
        Q(fk_patient__number_of_medical_card__icontains=search_query) |
        Q(diseases__name_disease__icontains=search_query))
    else:
        elements = MedicalRecord.objects.all()
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Возникла ошибка'
    form = MedicalRecordForm()
    context = {'elements': elements, 'form': form}
    return render(request, 'app/doctor/MedicalRecord.html', context)

class medicalRecordUpdateView(View):

    def get(self, request, id):
        medicalRecord = MedicalRecord.objects.get(pk=id)
        elements = MedicalRecord.objects.all()
        form = MedicalRecordForm(instance = medicalRecord)
        return render(request, 'app/doctor/MedicalRecord.html', context = {'form': form, 'data':medicalRecord , 'elements': elements} )

    def post(self, request, id):
        medicalRecord = MedicalRecord.objects.get(pk=id)
        form = MedicalRecordForm(request.POST, instance = medicalRecord)
        if form.is_valid():
            form.save()
            return redirect(medicalRecord)
        form = MedicalRecordForm()
        return render(request, 'app/doctor/MedicalRecord.html', context = {'form': form, 'data':medicalRecord} )

# Удаление
class medicalRecordDeleteView(DeleteView):
    model = MedicalRecord
    success_url = '/medicalRecord'
    template_name = 'app/doctor/DELETE.html'



# Рекомендации -------------------------------------------------------
def recommendation(request):
    error = ''
    search_query = request.GET.get('search','')
    if search_query:
        elements = Recommendation.objects.filter(Q(description_recommendation__icontains=search_query) |
        Q(fk_distribution__patients__surname_patient__icontains=search_query) |
        Q(fk_distribution__patients__name_patient__icontains=search_query) |
        Q(fk_distribution__patients__middlename_patient_icontains=search_query) | 
        Q(fk_distribution__surname_doctor__icontains=search_query) |
        Q(fk_distribution__name_doctor__icontains=search_query) |
        Q(fk_distribution__middlename_doctor__icontains=search_query) |
        Q(date_recommendation__icontains=search_query) |
        Q(period_recommendation__icontains=search_query))
    else:
        elements = Recommendation.objects.all()
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Возникла ошибка'
    form = RecommendationForm()
    context = {'elements': elements, 'form': form}
    return render(request, 'app/doctor/Recommendation.html', context)

class recommendationUpdateView(View):

    def get(self, request, id):
        recommendation = Recommendation.objects.get(pk=id)
        elements = Recommendation.objects.all()
        form = RecommendationForm(instance = recommendation)
        return render(request, 'app/doctor/Recommendation.html', context = {'form': form, 'data':recommendation, 'elements': elements})

    def post(self, request, id):
        recommendation = Recommendation.objects.get(pk=id)
        form = RecommendationForm(request.POST, instance = recommendation)
        if form.is_valid():
            form.save()
            return redirect(recommendation)
        form = RecommendationForm()
        return render(request, 'app/doctor/Recommendation.html', context = {'form': form, 'data': recommendation})

# Удаление
class recommendationDeleteView(DeleteView):
    model = Recommendation
    success_url = '/recommendation'
    template_name = 'app/doctor/DELETE.html'


def patient(request):
    error = ''
    elements = Patient.objects.all()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Возникла ошибка'
    form = PatientForm()
    context = {'elements': elements, 'form': form}
    return render(request, 'app/doctor/Patient.html', context)

class patientUpdateView(View):

    def get(self, request, id):
        patient = Patient.objects.get(pk=id)
        elements = Patient.objects.all()
        form = PatientForm(instance = patient)
        return render(request, 'app/doctor/Patient.html', context = {'form': form, 'data':patient, 'elements': elements})

    def post(self, request, id):
        patient = Patient.objects.get(pk=id)
        form = PatientForm(request.POST, instance = patient)
        if form.is_valid():
            form.save()
            return redirect('/patient')
        form = PatientForm()
        return render(request, 'app/doctor/Patient.html', context = {'form': form, 'data': patient})

#Подробности
class patientDetailView(DetailView):
    model = Patient
    template_name = 'app/result_patient.html'
    context_object_name = 'patient'

# Удаление
class patientDeleteView(DeleteView):
    model = Patient
    success_url = '/patient'
    template_name = 'app/doctor/DELETE.html'
#------------------------------------------------------- Конец Справочников -------------------------------------------------------




# ПАЦИЕНТ
def index(request):
    return render(request, 'app/index.html')


def personal_data(request):
    error = ''
    elements = Patient.objects.all()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Возникла ошибка'
    form = PatientForm()
    context = {'elements': elements, 'form': form}
    return render(request, 'app/diagnost_patient.html', context)

class result_patient(DeleteView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/result_patient.html'

# class processView(View):

#     def get(self, request, pk):
#         patient = Patient.objects.get(pk=pk)
#         elements = Patient.objects.all()
#         form = PatientProcessForm()
#         context = {'form': form,'elements': elements,'patient': patient}
#         return render(request, 'app/diagnost_process.html', context)

#     def post(self, request, pk):
#         patient = Patient.objects.get(pk=pk)
#         form = PatientProcessForm(request.POST)
#         if form.is_valid():
#             new = form.save()
#             return redirect(new)
#         form = PatientProcessForm()
#         return render(request, 'app/diagnost_process.html', context = {'form': form})

# def patient(request):
#     data_patient = Patient.objects.order_by()[:1] #вывод только первого пациента
#     return render(request, 'app/patient.html', {'data_patient': data_patient}) 




