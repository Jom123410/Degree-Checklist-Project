from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import (CourseForm, SemesterForm, DegreeProgramForm, StudentForm, 
                    AdviserForm, DegreeRequirementForm, CourseEnrollmentForm, UploadFileForm)
from .models import (Course, Semester, DegreeProgram, Student, Adviser, 
                     DegreeRequirement, CourseEnrollment, UploadedDataFile, Schedule)
from .services import (add_courses_to_schedule, process_uploaded_file, generate_schedule, enroll_student_in_course,  
                       get_current_academic_year, assign_adviser_to_student, get_current_semester, calculate_total_credits,
                       update_student, delete_student, check_prerequisites, calculate_degree_progress)
from django.views.generic import ListView, DetailView
import json

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # Handle the file processing here, e.g., importing data into the database
            # For now, let's assume you have a function called `handle_uploaded_file`
            handle_uploaded_file(instance.file)
            return redirect('some_view_name')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    # This function will handle your file, you can use Python's built-in CSV or 
    # other libraries to parse and import the data into your models
    pass


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


def get_current_academic_year():
    # Assuming the academic year starts in September
    current_year = datetime.now().year
    current_month = datetime.now().month

    # If the current month is January to August, the academic year began last year
    if current_month < 9:
        return current_year - 1
    else:
        return current_year
        
    
def get_current_semester():
    # Assuming two semesters: Spring (January to May) and Fall (September to December)
    current_month = datetime.now().month

    if 1 <= current_month <= 5:
        return "Spring"
    elif 9 <= current_month <= 12:
        return "Fall"
    else:
        return "Summer"  # Assuming Summer for the remaining months; adjust as needed

    
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

def course_selection(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'course_selection.html', {'courses': courses})

    if request.method == 'POST':
        # Get the list of selected course IDs from the form
        selected_courses = request.POST.getlist('selected_courses')
        schedule, created = Schedule.objects.get_or_create(
            student=request.user.student,
            academic_year=request.POST['academic_year'],
            semester=request.POST['semester']
        )

        for course_id in selected_courses:
            course = Course.objects.get(id=course_id)
            # Here you would include logic to check prerequisites, scheduling conflicts, etc.
            schedule.courses.add(course)
        
        messages.success(request, 'Courses have been added to your schedule.')
        return redirect('schedule_view')  # Redirect to the view that displays the schedule

    return render(request, 'course_selection.html')


def get_current_academic_year():
    current_year = datetime.now().year
    current_month = datetime.now().month
    return current_year - 1 if current_month < 9 else current_year

def get_current_semester():
    current_month = datetime.now().month
    if 1 <= current_month <= 5:
        return "Spring"
    elif 9 <= current_month <= 12:
        return "Fall"
    else:
        return "Summer"

def schedule_builder(request, academic_year=None, semester=None):
    # Set default values if they are None
    academic_year = academic_year or get_current_academic_year()
    semester = semester or get_current_semester()

    # Check if the user has an associated student
    try:
        student = request.user.student
    except Student.DoesNotExist:
        # Redirect to a different page or show an error message
        return redirect('home')  # Replace 'error_page' with an appropriate error page URL name

    # Fetch the Schedule object and render the page
    schedule, created = Schedule.objects.get_or_create(
        student=student,
        academic_year=academic_year,
        semester=semester
    )

    return render(request, 'schedule_builder.html', {
        'schedule': schedule,
        'academic_year': academic_year,
        'semester': semester
    })

def update_schedule(request):
    # Ensure that an 'application/json' content type is being sent with the request
    if request.content_type != 'application/json':
        return JsonResponse({'status': 'error', 'message': 'Invalid content type'}, status=400)
    
    # Parse the JSON data from the request
    try:
        data = json.loads(request.body)
        course_id = data.get('course_id')
        new_semester = data.get('new_semester')
    except (KeyError, ValueError) as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid data provided'}, status=400)

    # Get the course and schedule objects
    course = get_object_or_404(Course, id=course_id)
    student = get_object_or_404(Student, user=request.user)
    schedule, created = Schedule.objects.get_or_create(student=student, semester=new_semester)

    # Check if the course is already in the schedule for the semester
    if course not in schedule.courses.all():
        # Update the schedule to include the course
        schedule.courses.add(course)
        schedule.save()
        return JsonResponse({'status': 'success', 'message': 'Schedule updated successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Course is already in the schedule for this semester'}, status=400)
    
def save_schedule(request):
    # Implement your logic here
    # This might include saving a schedule to the database or performing other actions
    return JsonResponse({'status': 'success', 'message': 'Schedule saved successfully'})

def error_page(request, error_message):
    return render(request, 'error_page.html', {'error_message': error_message})
   
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
