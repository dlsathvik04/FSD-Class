from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from hobbies.forms import StudentForm, StudentHobbiesForm
from hobbies.models import StudentHobbies

# Create your views here.

def hobbiesForm(req : HttpRequest):
    if req.method == 'POST':
        StudentHobbies.objects.create(name = req.POST['name'], phone=req.POST['phone'], hobbies= req.POST['hobbies'])
    all_hobbies = StudentHobbies.objects.all()
    return render(req, 'hobbies.html' , {'hobbies' : all_hobbies})

def studentsForm(req: HttpRequest):
    stf = StudentForm()
    return render(req, 'students.html', {'studentForm' : stf})

def deleteHobbies(req : HttpRequest, pk):
    curr_student = StudentHobbies.objects.get(pk=pk)
    curr_student.delete()
    all_hobbies = StudentHobbies.objects.all()
    return render(req, 'hobbies.html' , {'hobbies' : all_hobbies})

def editHobbies(req : HttpRequest, pk):
    curr_student = StudentHobbies.objects.get(pk=pk)
    if req.method == 'GET':
        edit_form = StudentHobbiesForm(instance=curr_student)
        return render(req, 'hobbies_edit.html', {'studentHobbiesForm' : edit_form})
    if req.method == 'POST':
        name = req.POST['name']
        phone=req.POST['phone']
        hobbies= req.POST['hobbies']
        curr_student.name = name
        curr_student.phone = phone
        curr_student.hobbies = hobbies
        curr_student.save()
        all_hobbies = StudentHobbies.objects.all()
        return render(req, 'hobbies.html' , {'hobbies' : all_hobbies})