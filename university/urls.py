from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("student/", views.new_student, name="new_student"),
    path("students/<int:student_id>/", views.student_view, name="student_view"),
    path("students/", views.students, name="students"),
    path("teacher/", views.new_teacher, name="new_teacher"),
    path("teachers/<int:teacher_id>/", views.teacher_view, name="teacher_view"),
    path("teachers/", views.teachers, name="teachers"),
    path("students_groups/", views.students_groups, name="students_groups"),
]
