from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def validator_student(request):
    ESFO=StudentForm()
    d={'ESF':ESFO}
    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('student data inserted')
        else:
            return HttpResponse('invalid student data')    

    return render(request,'validator_student.html',d)