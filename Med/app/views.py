from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.contrib.auth import authenticate, login
from account.models import *
from app.models import *
from app.forms import *
from django.views.generic.base import RedirectView
from django.views.generic import View, DeleteView, DetailView, UpdateView
from django.db.models import Q
from django.core.mail import send_mail
import xlwt
from django.http import HttpResponse

def export_users_xls(request, pk):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения','Пол', 'СП', 
    'Номер мед карты', 'Симптомы','Болезни в детстве','Болезни родственников',
    'Хронические заболевания','Описание рекомендации','дата назначения','Период','Врач' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Patient.objects.filter(pk__in=[pk]).values_list('surname_patient', 'name_patient', 
    'middlename_patient', 'birthday_patient','gender_patient','enlightenment_patient','number_of_medical_card',
    'symptoms_patient__name_symptom','childhood_diseases__name_disease','relatives_diseases__name_disease',
    'chronic_disease','description_recommendation','date_recommendation','period_recommendation','fk_account__surname_doctor')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response



def inform(request, pk):
    error = ''
    inform = Patient.objects.get(pk=pk)
    form = InformForm(request.POST or None)
    if form.is_valid():
        form.save()
        send_mail(form.cleaned_data['topic'],form.cleaned_data['problem_description'],
        'edx860@gmail.com',[form.cleaned_data['email_addres']], fail_silently=False)
        return redirect ('/')
    else:
        error = 'Возникла ошибка'

    form = InformForm()
    context = {'form': form,'inform':inform}
    return render(request, 'app/inform_patient.html', context)

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
        info = Patient.objects.filter(Q(surname_patient__icontains=search_query) | 
        Q(name_patient__icontains=search_query) | 
        Q(middlename_patient__icontains=search_query) |
        Q(number_of_medical_card__icontains=search_query) |
        Q(enlightenment_patient__icontains=search_query) |
        Q(symptoms_patient__name_symptom__icontains=search_query) |
        Q(birthday_patient__icontains=search_query))
    else:
        info = Patient.objects.filter(fk_account__in=[user_id])
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
        elements = Patient.objects.filter(Q(surname_patient__icontains=search_query) |
        Q(name_patient__icontains=search_query) |
        Q(middlename_patient__icontains=search_query) | 
        Q(symptoms_patient__name_symptom__icontains=search_query) |
        Q(number_of_medical_card__icontains=search_query) |
        Q(gender_patient__icontains=search_query))
    else:
        elements = Patient.objects.all()
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
        medicalRecord = Patient.objects.get(pk=id)
        elements = Patient.objects.all()
        form = MedicalRecordForm(instance = medicalRecord)
        return render(request, 'app/doctor/MedicalRecord.html', context = {'form': form, 'data':medicalRecord , 'elements': elements} )

    def post(self, request, id):
        medicalRecord = Patient.objects.get(pk=id)
        form = MedicalRecordForm(request.POST, instance = medicalRecord)
        if form.is_valid():
            form.save()
            return redirect(medicalRecord)
        form = MedicalRecordForm()
        return render(request, 'app/doctor/MedicalRecord.html', context = {'form': form, 'data': medicalRecord} )

# Удаление
class medicalRecordDeleteView(DeleteView):
    model = Patient
    success_url = '/medicalRecord'
    template_name = 'app/doctor/DELETE.html'



# Рекомендации -------------------------------------------------------
def recommendation(request):
    error = ''
    search_query = request.GET.get('search','')
    if search_query:
        elements = Patient.objects.filter(Q(description_recommendation__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(name_patient__icontains=search_query) |
        Q(middlename_patient__icontains=search_query) | 
        Q(surname_patient__icontains=search_query) | 
        Q(fk_account__surname_doctor__icontains=search_query) |
        Q(fk_account__name_doctor__icontains=search_query) |
        Q(fk_account__middlename_doctor__icontains=search_query) |
        Q(birthday_patient__icontains=search_query) |
        Q(number_of_medical_card__icontains=search_query) |
        Q(gender_patient__icontains=search_query) |
        Q(symptoms_patient__name_symptom__icontains=search_query) |
        Q(childhood_diseases__name_disease__icontains=search_query) |
        Q(relatives_diseases__name_disease__icontains=search_query) |
        Q(chronic_disease__icontains=search_query))
    else:
        elements = Patient.objects.all()
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
        recommendation = Patient.objects.get(pk=id)
        elements = Patient.objects.all()
        form = RecommendationForm(instance = recommendation)
        return render(request, 'app/doctor/Recommendation.html', context = {'form': form, 'data':recommendation, 'elements': elements})

    def post(self, request, id):
        recommendation = Patient.objects.get(pk=id)
        form = RecommendationForm(request.POST, instance = recommendation)
        if form.is_valid():
            form.save()
            return redirect('recommendation')
        form = RecommendationForm()
        return render(request, 'app/doctor/Recommendation.html', context = {'form': form, 'data': recommendation})

# Удаление
class recommendationDeleteView(DeleteView):
    model = Patient
    success_url = '/recommendation'
    template_name = 'app/doctor/DELETE.html'

def patient(request):
    error = ''
    search_query = request.GET.get('search','')
    if search_query:
        elements = Patient.objects.filter(Q(description_recommendation__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(name_patient__icontains=search_query) |
        Q(middlename_patient__icontains=search_query) | 
        Q(surname_patient__icontains=search_query) | 
        Q(number_of_medical_card__icontains=search_query) |
        Q(gender_patient__icontains=search_query) |
        Q(symptoms_patient__name_symptom__icontains=search_query) |
        Q(childhood_diseases__name_disease__icontains=search_query) |
        Q(relatives_diseases__name_disease__icontains=search_query) |
        Q(chronic_disease__icontains=search_query))
    else:
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
    form_class = PatientForm
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
            return redirect('welldone')
        else:
            error = 'Возникла ошибка'
    form = PatientForm()
    context = {'elements': elements, 'form': form}
    return render(request, 'app/diagnost_patient.html', context)

class result_patient(DeleteView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/result_patient.html'

def logout_view(request):
    logout(request)
    return redirect('index')


def welldone(request):
    return render(request, 'app/welldone.html')




