from django.urls import path
from . import views


urlpatterns = [
    # Если пользователь перешёл на главную страницу, то нужно вызвать метод views
    # После этого прописываем метод в файле views.py
    # После точки указываем нужный метод в файле views.py
    # path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    # path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('auth', views.auth, name='auth'),
    path('profile', views.profile, name='profile'),
    path('inform/<int:pk>', views.inform, name='inform'),


    path('disease', views.disease, name='disease'),
    path('disease/<int:id>/update', views.diseaseUpdateView.as_view(), name='disease_update'),
    path('disease/<int:pk>/delete', views.diseaseDeleteView.as_view(), name='disease_delete'),

    path('symptom', views.symptom, name='symptom'),
    path('symptom/<int:id>/update', views.symptomUpdateView.as_view(), name='symptom_update'),
    path('symptom/<int:pk>/delete', views.symptomDeleteView.as_view(), name='symptom_delete'),

    path('medicalRecord', views.medicalRecord, name='medicalRecord'),
    path('medicalRecord/<int:id>/update', views.medicalRecordUpdateView.as_view(), name='medicalRecord_update'),
    path('medicalRecord/<int:pk>/delete', views.medicalRecordDeleteView.as_view(), name='medicalRecord_delete'),

    path('recommendation', views.recommendation, name='recommendation'),
    path('recommendation/<int:id>/update', views.recommendationUpdateView.as_view(), name='recommendation_update'),
    path('recommendation/<int:pk>/delete', views.recommendationDeleteView.as_view(), name='recommendation_delete'),

    path('patient', views.patient, name='patient'),
    path('patient/<int:id>/update', views.patientUpdateView.as_view(), name='patient_update'),
    path('patient/<int:pk>/detail', views.patientDetailView.as_view(), name='patient_detail'),
    path('patient/<int:pk>/delete', views.patientDeleteView.as_view(), name='patient_delete'),
    # path('patient/<int:id>/create', views.patientRecomendationCreateView.as_view(), name='recomendation_create'),

    path('export_users_xls/<int:pk>', views.export_users_xls, name='export_users_xls'),

# Пациент -------------------------------------------------------------------------------

    path('personal_data', views.personal_data, name='personal_data'),
    path('result_patient/<int:pk>/detail', views.result_patient.as_view(), name='result_patient'),
    
    # path('process/<int:pk>', views.processView.as_view(), name='process'),
]
