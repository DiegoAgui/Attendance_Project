from django.db import models

class Cohorte(models.Model):
    name = models.CharField(max_length=50)
    group_director = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    number_students_initial = models.IntegerField(default=0)