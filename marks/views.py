from django.http import HttpRequest
from django.shortcuts import render

from marks.models import StudentMarks

# Create your views here.

def marksForm(req : HttpRequest):
    if req.method == 'POST':
        name = req.POST['name']
        maths = req.POST['maths']
        physics = req.POST['physics']
        chemistry = req.POST['chemistry']
        StudentMarks.objects.create(name = name, maths = maths, physics = physics, chemistry = chemistry)
        print(req.POST)
    return render(req, 'marks.html')