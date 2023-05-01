from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ["first_name"]


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ["first_name"]


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    students = models.ManyToManyField(Student)

    class Meta:
        ordering = ["group_name"]
