from django.db import models
from datetime import datetime, timedelta

# Create your models here.


def dueDate():
    return datetime.today() + timedelta(days=7)

class To_DO_List(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class List(models.Model):
    title = models.CharField(max_length=100 )
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=dueDate)
    To_DoList = models.ForeignKey(To_DO_List(), on_delete=models.CASCADE)

   
    def __str__(self):
        return str(self.title) 

