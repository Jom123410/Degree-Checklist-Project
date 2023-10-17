from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView
from .models import Student, DegreeProgram, Course, Adviser, DegreeRequirement, CourseEnrollment
from .forms import StudentForm, CourseForm, Semester

def home(request):
    return render(request, "home.html")

# Student views
class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"

class SemesterListView(ListView):
    model = Semester  # Specify the model you want to work with.
    template_name = 'semester_list.html'  # Specify the name of the template to render. You can change this to your desired template name.
    context_object_name = 'semesters'     

class SemesterDetailView(DetailView):
    model = Semester
    template_name = 'degree_checklist/semester_detail.html'  # Update this to the path of your desired template
    context_object_name = 'semester'
    
class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')  # Redirect to some view after successfully adding a student
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redirect to the list of courses after adding a course
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})

def add_semester(request):
    if request.method == 'POST':
        form = Semester(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')  # Redirect to the list of semesters after adding a semester
    else:
        form = Semester()

    return render(request, 'add_semester.html', {'form': form})

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
