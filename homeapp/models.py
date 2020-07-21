from django.db import models

class Lecture(models.Model):
    professor = models.CharField(max_length=50)
    rq_year = models.IntegerField()
    rq_semester = models.IntegerField()
    department = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    instruction_number = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    credit = models.IntegerField()
    time = models.IntegerField()
