from django.urls import path
from . import views


urlpatterns = [
    # Если пользователь перешёл на главную страницу, то нужно вызвать метод views
    # После этого прописываем метод в файле views.py
    # После точки указываем нужный метод в файле views.py
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('auth', views.auth, name='auth'),
    path('profile', views.profile, name='profile'),
    

    path('disease', views.disease, name='disease'),
    path('disease/<int:id>/update', views.diseaseUpdateView.as_view(), name='disease_update'),
    path('disease/<int:pk>/delete', views.diseaseDeleteView.as_view(), name='disease_delete'),

    # path('distribution', views.distribution, name='distribution'),
    # path('distribution/<int:id>/update', views.distributionUpdateView.as_view(), name='distribution_update'),
    # path('distribution/<int:pk>/delete', views.distributionDeleteView.as_view(), name='distribution_delete'),

    path('symptom', views.symptom, name='symptom'),
    path('symptom/<int:id>/update', views.symptomUpdateView.as_view(), name='symptom_update'),
    path('symptom/<int:pk>/delete', views.symptomDeleteView.as_view(), name='symptom_delete'),

    path('medicalRecord', views.medicalRecord, name='medicalRecord'),
    path('medicalRecord/<int:id>/update', views.medicalRecordUpdateView.as_view(), name='medicalRecord_update'),
    path('medicalRecord/<int:pk>/delete', views.medicalRecordDeleteView.as_view(), name='medicalRecord_delete'),

    path('recommendation', views.recommendation, name='recommendation'),
    path('recommendation/<int:id>/update', views.recommendationUpdateView.as_view(), name='recommendation_update'),
    path('recommendation/<int:pk>/delete', views.recommendationDeleteView.as_view(), name='recommendation_delete'),


# Пациент -------------------------------------------------------------------------------
    # path('personal_data', views.personal_data, name='personal_data'),
    path('personal_data', views.personal_data, name='personal_data'),
    path('patient', views.patient, name='patient'),
    path('result_patient/<int:pk>/detail', views.result_patient.as_view(), name='result_patient'),
    # path('process/<int:pk>', views.processView.as_view(), name='process'),
]
