from django.shortcuts import get_object_or_404, render, redirect
from .forms import (CourseForm, SemesterForm, DegreeProgramForm, StudentForm, 
                   AdviserForm, DegreeRequirementForm, CourseEnrollmentForm)
from .models import Course, Semester, DegreeProgram, Student, Adviser, DegreeRequirement, CourseEnrollment
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, "home.html")

def form_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or any other URL after successful form submission.
    else:
        form = StudentForm()

    return render(request, 'form_page.html', {'form': form})

# Create views
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

def create_semester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm()
    return render(request, 'create_semester.html', {'form': form})

def create_degree_program(request):
    if request.method == 'POST':
        form = DegreeProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('degree_program_list')
    else:
        form = DegreeProgramForm()
    return render(request, 'create_degree_program.html', {'form': form})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def create_adviser(request):
    if request.method == 'POST':
        form = AdviserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adviser_list')
    else:
        form = AdviserForm()
    return render(request, 'create_adviser.html', {'form': form})

def create_degree_requirement(request):
    if request.method == 'POST':
        form = DegreeRequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('degreerequirement_list')
    else:
        form = DegreeRequirementForm()
    return render(request, 'create_degree_requirement.html', {'form': form})

def create_course_enrollment(request):
    if request.method == 'POST':
        form = CourseEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_enrollment_list')
    else:
        form = CourseEnrollmentForm()
    return render(request, 'create_course_enrollment.html', {'form': form})

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


# List and Detail views
class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"

class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"

class SemesterListView(ListView):
    model = Semester
    template_name = 'semester_list.html'
    context_object_name = 'semesters'     

class SemesterDetailView(DetailView):
    model = Semester
    template_name = 'semester_detail.html'
    context_object_name = 'semester'

class DegreeProgramListView(ListView):
    model = DegreeProgram
    template_name = "degreeprogram_list.html"

class DegreeProgramDetailView(DetailView):
    model = DegreeProgram
    template_name = "degreeprogram_detail.html"

class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"

class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"

class AdviserListView(ListView):
    model = Adviser
    template_name = "adviser_list.html"

class AdviserDetailView(DetailView):
    model = Adviser
    template_name = "adviser_detail.html"

class DegreeRequirementListView(ListView):
    model = DegreeRequirement
    template_name = "degreerequirement_list.html"

class DegreeRequirementDetailView(DetailView):
    model = DegreeRequirement
    template_name = "degreerequirement_detail.html"

class CourseEnrollmentListView(ListView):
    model = CourseEnrollment
    template_name = "courseenrollment_list.html"

class CourseEnrollmentDetailView(DetailView):
    model = CourseEnrollment
    template_name = "courseenrollment_detail.html"

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')  # Redirect to the list of students after updating
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list')
    return render(request, 'confirm_delete.html', {'object': student})

# Custom Student List
def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})  

# Update DegreeProgram
def update_degree_program(request, pk):
    degree_program = get_object_or_404(DegreeProgram, pk=pk)
    
    if request.method == 'POST':
        form = DegreeProgramForm(request.POST, instance=degree_program)
        if form.is_valid():
            form.save()
            return redirect('degreeprogram-list')
    else:
        form = DegreeProgramForm(instance=degree_program)
        
    return render(request, 'update_degree_program.html', {'form': form})

# Delete DegreeProgram
def delete_degree_program(request, pk):
    degree_program = get_object_or_404(DegreeProgram, pk=pk)
    if request.method == 'POST':
        degree_program.delete()
        return redirect('degreeprogram-list')
    return render(request, 'confirm_delete.html', {'object': degree_program})

# Custom DegreeProgram List
def list_degree_programs(request):
    degree_programs = DegreeProgram.objects.all()
    return render(request, 'list_degree_programs.html', {'degree_programs': degree_programs})

# Update Course
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form = CourseForm(instance=course)
        
    return render(request, 'update_course.html', {'form': form})

# Delete Course
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course-list')
    return render(request, 'confirm_delete.html', {'object': course})

# Custom Course List
def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'list_courses.html', {'courses': courses})

# Update Semester
def update_semester(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('semester-list')
    else:
        form = SemesterForm(instance=semester)
        
    return render(request, 'update_semester.html', {'form': form})

# Delete Semester
def delete_semester(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    if request.method == 'POST':
        semester.delete()
        return redirect('semester-list')
    return render(request, 'confirm_delete.html', {'object': semester})

# Custom Semester List
def list_semesters(request):
    semesters = Semester.objects.all()
    return render(request, 'list_semesters.html', {'semesters': semesters})

# Update Adviser
def update_adviser(request, pk):
    adviser = get_object_or_404(Adviser, pk=pk)
    
    if request.method == 'POST':
        form = AdviserForm(request.POST, instance=adviser)
        if form.is_valid():
            form.save()
            return redirect('adviser-list')
    else:
        form = AdviserForm(instance=adviser)
        
    return render(request, 'update_adviser.html', {'form': form})

# Delete Adviser
def delete_adviser(request, pk):
    adviser = get_object_or_404(Adviser, pk=pk)
    if request.method == 'POST':
        adviser.delete()
        return redirect('adviser-list')
    return render(request, 'confirm_delete.html', {'object': adviser})

# Custom Adviser List
def list_advisers(request):
    advisers = Adviser.objects.all()
    return render(request, 'list_advisers.html', {'advisers': advisers})

# Update DegreeRequirement
def update_degree_requirement(request, pk):
    degree_requirement = get_object_or_404(DegreeRequirement, pk=pk)
    
    if request.method == 'POST':
        form = DegreeRequirementForm(request.POST, instance=degree_requirement)
        if form.is_valid():
            form.save()
            return redirect('degreerequirement-list')
    else:
        form = DegreeRequirementForm(instance=degree_requirement)
        
    return render(request, 'update_degree_requirement.html', {'form': form})

# Delete DegreeRequirement
def delete_degree_requirement(request, pk):
    degree_requirement = get_object_or_404(DegreeRequirement, pk=pk)
    if request.method == 'POST':
        degree_requirement.delete()
        return redirect('degreerequirement-list')
    return render(request, 'confirm_delete.html', {'object': degree_requirement})

# Custom DegreeRequirement List
def list_degree_requirements(request):
    degree_requirements = DegreeRequirement.objects.all()
    return render(request, 'list_degree_requirements.html', {'degree_requirements': degree_requirements})

# Update CourseEnrollment
def update_course_enrollment(request, pk):
    course_enrollment = get_object_or_404(CourseEnrollment, pk=pk)
    
    if request.method == 'POST':
        form = CourseEnrollmentForm(request.POST, instance=course_enrollment)
        if form.is_valid():
            form.save()
            return redirect('courseenrollment-list')
    else:
        form = CourseEnrollmentForm(instance=course_enrollment)
        
    return render(request, 'update_course_enrollment.html', {'form': form})

# Delete CourseEnrollment
def delete_course_enrollment(request, pk):
    course_enrollment = get_object_or_404(CourseEnrollment, pk=pk)
    if request.method == 'POST':
        course_enrollment.delete()
        return redirect('courseenrollment-list')
    return render(request, 'confirm_delete.html', {'object': course_enrollment})

# Custom CourseEnrollment List
def list_course_enrollments(request):
    course_enrollments = CourseEnrollment.objects.all()
    return render(request, 'list_course_enrollments.html', {'course_enrollments': course_enrollments})
