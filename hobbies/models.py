from django.db import models

# Create your models here.
class StudentHobbies(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    hobbies = models.TextField()

class Student(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
    GENDER = {
        'M' : "Male",
        "F" : "Female"
    }
    name = models.CharField(max_length=40)
    batch = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
