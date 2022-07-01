from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, blank=True)


class Picture(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')


class File(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files')


class Department(models.Model):
    title = models.CharField(max_length=100)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)


