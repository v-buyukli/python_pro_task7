from django.contrib import admin

from .models import Group, Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ordering = ["first_name"]
    list_filter = ["first_name", "last_name", "age"]
    list_display = ["first_name", "last_name", "age"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    ordering = ["first_name"]
    list_filter = ["first_name", "last_name", "age"]
    list_display = ["first_name", "last_name", "age"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ordering = ["group_name"]
    list_filter = ["group_name"]
    list_display = ["group_name"]
