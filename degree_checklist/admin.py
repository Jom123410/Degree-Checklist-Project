from django.contrib import admin
from .models import Student, DegreeProgram, Course, Adviser, DegreeRequirement, CourseEnrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'email', 'phone']
    # Add other customization options as needed

@admin.register(DegreeProgram)
class DegreeProgramAdmin(admin.ModelAdmin):
    list_display = ['program_id', 'program_name', 'department', 'total_credits_required']
    # Add other customization options as needed

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'course_code', 'course_name', 'credits']
    # Add other customization options as needed

@admin.register(Adviser)
class AdviserAdmin(admin.ModelAdmin):
    list_display = ['adviser_id', 'first_name', 'last_name', 'email', 'phone', 'department']
    # Add other customization options as needed

@admin.register(DegreeRequirement)
class DegreeRequirementAdmin(admin.ModelAdmin): 
    list_display = ['requirement_id', 'program', 'course', 'credits_required']
    # Add other customization options as needed

@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['enrollment_id', 'student', 'course', 'enrollment_date', 'grade']
    # Add other customization options as needed