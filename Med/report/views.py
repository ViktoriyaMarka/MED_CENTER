from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from report.models import *
from report.forms import *
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.

def report(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/register')

    error = ''
    form = ReportForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        topic = request.POST['topic']
        problem_description = request.POST['problem_description']

        send_mail(topic,problem_description,'edx860@gmail.com',['edx860@gmail.com'],
        fail_silently=False)
        return redirect('/')
    else:
        error = 'Возникла ошибка'

    form = ReportForm()
    context = {'form': form}
    return render(request, 'report/report.html', context)
