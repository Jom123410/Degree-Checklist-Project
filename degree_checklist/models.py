from django.db import models

# Create your models here.
 # Define the Student model
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    # Add other fields here

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Define the DegreeProgram model
class DegreeProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    total_credits_required = models.IntegerField()
    duration_in_years = models.IntegerField()
    program_description = models.TextField()
    # Add other fields here

    def __str__(self):
        return self.program_name

# Define the Course model
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    prerequisites = models.TextField()
    semester_offered = models.CharField(max_length=20)
    # Add other fields here

    def __str__(self):
        return self.course_code

# Define the Adviser model
class Adviser(models.Model):
    adviser_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    # Add other fields here

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Define the DegreeRequirement model
class DegreeRequirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    credits_required = models.IntegerField()
    # Add other fields here

# Define the CourseEnrollment model
class CourseEnrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=2)
    