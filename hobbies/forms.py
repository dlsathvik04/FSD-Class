
from django.forms import ModelForm

from hobbies.models import Student, StudentHobbies

class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields = ['name', 'batch', 'gender', 'shirt_size']

class StudentHobbiesForm(ModelForm):
    class Meta:
        model = StudentHobbies
        fields = ['name', 'phone', 'hobbies']
