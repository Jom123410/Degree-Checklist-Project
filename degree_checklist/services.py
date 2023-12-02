# services.py

from .models import (Course, Semester, DegreeProgram, Student, Adviser, 
                     DegreeRequirement, CourseEnrollment, UploadedDataFile, Schedule)
from django.shortcuts import get_object_or_404
from datetime import datetime

def check_prerequisites(student, course):
    # Check if student has completed all prerequisites for the course
    completed_courses = set(student.courseenrollment_set.filter(grade='P').values_list('course', flat=True))
    prerequisites = course.prerequisites.all()
    return all(prereq.id in completed_courses for prereq in prerequisites)

def calculate_degree_progress(student):
    # Calculate progress towards degree completion based on earned credits
    if not student.degree_program:
        return 0
    total_credits = student.degree_program.total_credits_required
    earned_credits = sum(enrollment.course.credits for enrollment in student.courseenrollment_set.filter(grade='P') if enrollment.course)
    return (earned_credits / total_credits) * 100

def add_courses_to_schedule(student, selected_course_ids, academic_year, semester):
    schedule, created = Schedule.objects.get_or_create(
        student=student,
        academic_year=academic_year,
        semester=semester
    )

    for course_id in selected_course_ids:
        course = Course.objects.get(id=course_id)
        if check_prerequisites(student, course):
            schedule.courses.add(course)

def enroll_student_in_course(student, course, semester):
    # Enroll a student in a course after checking prerequisites and conflicts
    if not check_prerequisites(student, course):
        return "Prerequisite not satisfied"
    
    # Additional checks for conflicts can be implemented here

    CourseEnrollment.objects.create(student=student, course=course, semester=semester)
    return "Enrollment successful"

def generate_schedule(student, semester):
    # Generate a course schedule for a student for a given semester
    enrolled_courses = student.courseenrollment_set.filter(semester=semester)
    return enrolled_courses

def assign_adviser_to_student(student):
    
    adviser = Adviser.objects.first()
    student.advisor = adviser
    student.save()
    return adviser

def calculate_total_credits(student):
    # Calculate the total credits earned by a student
    return sum(enrollment.course.credits for enrollment in student.courseenrollment_set.filter(grade='P') if enrollment.course)

def add_courses_to_schedule(student, selected_course_ids, academic_year, semester):
    schedule, created = Schedule.objects.get_or_create(
        student=student,
        academic_year=academic_year,
        semester=semester
    )

    for course_id in selected_course_ids:
        course = Course.objects.get(id=course_id)
        # Include logic to check prerequisites, scheduling conflicts, etc.
        schedule.courses.add(course)

def process_uploaded_file(file):
    # Implement the logic to handle and process the uploaded file
    pass

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

def update_student(student_id, data):
    student = get_object_or_404(Student, pk=student_id)
    for field, value in data.items():
        setattr(student, field, value)
    student.save()

def delete_student(student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()