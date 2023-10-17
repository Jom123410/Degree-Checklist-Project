from django import forms
from .models import Student, Course, Semester

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code']

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = []
