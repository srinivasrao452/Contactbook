
from django.db import models

# from server side commit in model

class Employee(models.Model):

    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    salary = models.FloatField()

    def __str__(self):
        return self.ename


