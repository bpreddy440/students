from django.shortcuts import render, get_object_or_404
from .models import Student
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


def index(request):
    s = Student.objects.all()
    return render(request, 'students/index.html', context={'student':s})


def create(request):
    if request.method == "POST":
        # import pdb;pdb.set_trace()
        student=Student.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            mobile = request.POST['mobile'],
            email = request.POST['email'],
            dob = request.POST['dob'],
            nick_name = request.POST['nick_name'],

          )
        return HttpResponseRedirect(reverse('student:index'))
    return render(request, 'students/create_student.html')


def details(request, id):
    stu=get_object_or_404(Student, pk=id)
    return render(request, 'students/details.html', context={'student':stu})