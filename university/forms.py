from django import forms
from django.core.exceptions import ValidationError

import phonenumbers

from university.models import Student, Teacher, Group


def check_digits(string):
    return string.isalpha()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "age", "phone"]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not check_digits(first_name):
            raise ValidationError("Only letters are allowed for the student First name...")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not check_digits(last_name):
            raise ValidationError("Only letters are allowed for the student Last name...")
        return last_name

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 16:
            raise ValidationError("The minimum age for student is 16 years...")
        return age

    def clean_phone(self):
        phone_raw = self.cleaned_data["phone"]
        try:
            phone = phonenumbers.parse(phone_raw, "UA")
        except phonenumbers.NumberParseException:
            raise ValidationError("Phone is invalid...")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Phone is invalid...")
        return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "age"]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not check_digits(first_name):
            raise ValidationError("Only letters are allowed for the teacher First name...")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not check_digits(last_name):
            raise ValidationError("Only letters are allowed for the teacher Last name...")
        return last_name

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 22:
            raise ValidationError("The minimum age for teacher is 22 years...")
        return age


class GroupForm(forms.Form):
    student_id = forms.IntegerField(label="Student number", min_value=1)
    group_id = forms.IntegerField(label="Group number", min_value=1)

    def clean_student_id(self):
        student_id = self.cleaned_data["student_id"]
        if student_id not in list(Student.objects.all().values_list('id', flat=True)):
            raise ValidationError("This student does not exist....")
        return student_id

    def clean_group_id(self):
        group_id = self.cleaned_data["group_id"]
        group = Group.objects.get(id=group_id)
        student = Student.objects.get(id=GroupForm.clean_student_id(self))

        if group_id not in list(Group.objects.all().values_list('id', flat=True)):
            raise ValidationError("This group does not exist...")
        if student in group.students.all():
            raise ValidationError("This student is already in this group...")
        return group_id
