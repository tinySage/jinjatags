from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

# def register(request):
#     name = 'likith'
#     pno = 8179267926
#     email = 'likith.d@qspiders.in'
#     add = 'Lepakshi'
#     EO = Emp(ename = name, pno = pno, email = email, add = add)
#     EO.save()
#     return HttpResponse('Employee Registered Successfully')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('ename')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        EO = Emp(ename = name, pno = pno, email = email, add = add)
        EO.save()
        return HttpResponse('Employee Registered Successfully')
    return render(request, 'register.html')



def home(request):
    EO = Emp.objects.all()
    d = {'EmployeeObjects':EO}

    return render(request, 'home.html', d)