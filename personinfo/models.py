from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.first_name +' ' + self.last_name


class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return self.name