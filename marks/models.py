from django.db import models

# Create your models here.

class StudentMarks(models.Model):
    name = models.CharField(max_length=50)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
