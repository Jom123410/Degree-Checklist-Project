from django.contrib import admin
from .models import Student, DegreeProgram, Course, Adviser, DegreeRequirement, CourseEnrollment, Semester

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'email', 'phone']
    search_fields = ['first_name', 'last_name', 'email']
    # list_filter = ['enrollment_date']
    ordering = ['last_name', 'first_name']

@admin.register(DegreeProgram)
class DegreeProgramAdmin(admin.ModelAdmin):
    list_display = ['program_id', 'program_name', 'department', 'total_credits_required']
    search_fields = ['program_name', 'department']
    list_filter = ['department']
    ordering = ['program_name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'course_code', 'course_name', 'credits']
    search_fields = ['course_code', 'course_name']
    list_filter = ['course_code']
    ordering = ['course_code']

@admin.register(Adviser)
class AdviserAdmin(admin.ModelAdmin):
    list_display = ['adviser_id', 'first_name', 'last_name', 'email', 'phone', 'department']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['department']
    ordering = ['last_name', 'first_name']

@admin.register(DegreeRequirement)
class DegreeRequirementAdmin(admin.ModelAdmin):
    list_display = ['requirement_id', 'program', 'course', 'credits_required']
    search_fields = ['program__program_name', 'course__course_name']  # adjusted search fields
    list_filter = ['program']
    ordering = ['program']

@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['enrollment_id', 'student', 'course', 'enrollment_date', 'grade']
    search_fields = ['student__first_name', 'course__course_name']  # adjusted search fields
    list_filter = ['enrollment_date']
    ordering = ['enrollment_date']

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    
    # Search capability
    search_fields = ['name']
    
    # Filters
    list_filter = ['start_date', 'end_date']
    
    # Default ordering (ascending order on 'start_date')
    ordering = ['start_date']
    
    # Custom action
    actions = ['make_past_semesters']

    def make_past_semesters(self, request, queryset):
        queryset.update(end_date='2020-01-01')  # just an example to update end_date
        self.message_user(request, f"{queryset.count()} semesters were marked as past semesters.")
    make_past_semesters.short_description = "Mark selected semesters as past semesters"
