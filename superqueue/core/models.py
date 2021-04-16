from django.db import models


# Create your models here.
class Table(models.Model):
    table_name = models.CharField(max_length=50, unique=True)
    persons = models.ManyToManyField(to='Person', related_name='table_person')

    def __str__(self):
        return self.table_name


class Person(models.Model):

    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    time_waits = models.CharField(max_length=100)
    color_class = models.CharField(max_length=50, default="bg-light")
    def __str__(self):
        return self.name
