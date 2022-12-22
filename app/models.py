from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    sport = models.ManyToManyField(Sport)
    def __str__(self):
        return self.name



class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

