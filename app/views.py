from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *

def sf(request):
    SFO=StudentForms()
    d={'SFO':SFO} 
    if request.method=='POST':
        SFD=StudentForms(request.POST)
        if SFD.is_valid():
            return HttpResponse('<h1>data is valid</h1>')  
        else:
            return HttpResponse('<h1>data is not valid</h1>')

    return render(request,'sf.html',d)