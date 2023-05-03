from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from university.forms import StudentForm, TeacherForm, GroupForm
from university.models import Student, Teacher, Group


def index(request):
    name = "university"
    return render(request, "index.html", {"name": name})


def student_view(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            if "edit" in request.POST:
                form.save()
                return render(request, "student.html", {"form": form})
            elif "delete" in request.POST:
                student.delete()
                return HttpResponseRedirect(reverse("students"))
    else:
        form = StudentForm(instance=student)
    return render(request, "student.html", {"form": form})


def new_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("student_view", args=[form.instance.id]))
    else:
        form = StudentForm()
    return render(request, "new_student.html", {"form": form})


def students(request):
    students_list = list(Student.objects.all().values())
    return render(request, "students.html", {"students_list": students_list})


def teacher_view(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            if "edit" in request.POST:
                form.save()
                return render(request, "teacher.html", {"form": form})
            elif "delete" in request.POST:
                teacher.delete()
                return HttpResponseRedirect(reverse("teachers"))
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "teacher.html", {"form": form})


def new_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teacher_view", args=[form.instance.id]))
    else:
        form = TeacherForm()
    return render(request, "new_teacher.html", {"form": form})


def teachers(request):
    teachers_list = list(Teacher.objects.all().values())
    return render(request, "teachers.html", {"teachers_list": teachers_list})


def students_groups(request):
    groups_list = list(Group.objects.all().values())
    students_list = list(Student.objects.all().values())

    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            student_id = int(request.POST['student_id'])
            student = Student.objects.get(id=student_id)
            group_id = int(request.POST['group_id'])
            group = Group.objects.get(id=group_id)
            group.students.add(student)
            return HttpResponseRedirect(reverse("students_groups"))
    else:
        form = GroupForm()

    context = {
        "form": form,
        "groups_list": groups_list,
        "students_list": students_list,
    }
    return render(request, "students_groups.html", context)
