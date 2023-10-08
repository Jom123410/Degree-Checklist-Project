from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Student, DegreeProgram, Course, Adviser, DegreeRequirement, CourseEnrollment

def home(request):
    return render(request, "home.html")

# Student views
class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"

class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"

# DegreeProgram views
class DegreeProgramListView(ListView):
    model = DegreeProgram
    template_name = "degreeprogram_list.html"

class DegreeProgramDetailView(DetailView):
    model = DegreeProgram
    template_name = "degreeprogram_detail.html"

# Course views
class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"

class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"

# Adviser views
class AdviserListView(ListView):
    model = Adviser
    template_name = "adviser_list.html"

class AdviserDetailView(DetailView):
    model = Adviser
    template_name = "adviser_detail.html"

# DegreeRequirement views
class DegreeRequirementListView(ListView):
    model = DegreeRequirement
    template_name = "degreerequirement_list.html"

class DegreeRequirementDetailView(DetailView):
    model = DegreeRequirement
    template_name = "degreerequirement_detail.html"

# CourseEnrollment views
class CourseEnrollmentListView(ListView):
    model = CourseEnrollment
    template_name = "courseenrollment_list.html"

class CourseEnrollmentDetailView(DetailView):
    model = CourseEnrollment
    template_name = "courseenrollment_detail.html"
