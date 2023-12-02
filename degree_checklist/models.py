from django.db import models
from django.contrib.auth.models import User

class DegreeProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, null=True)
    total_credits_required = models.IntegerField(null=True)
    duration_in_years = models.IntegerField(null=True)
    program_description = models.TextField(null=True)

    def __str__(self):
        return self.program_name
    

class Adviser(models.Model):
    adviser_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Semester(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE, related_name='courses')
    course_code = models.CharField(max_length=20, null=True)
    course_name = models.CharField(max_length=100, null=True)
    credits = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    description = models.TextField(null=True)
    prerequisites = models.ManyToManyField('self', blank=True)
    semester_offered = models.CharField(max_length=20, null=True)
    

    def __str__(self):
        return self.course_name

    def is_prerequisite_satisfied(self, student):
        pass

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    degree_program = models.ForeignKey('DegreeProgram', on_delete=models.CASCADE, null=True)
    advisor = models.ForeignKey('Adviser', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_remaining_credits(self):
        total_credits = self.degree_program.total_credits_required if self.degree_program else 0
        earned_credits = sum(enrollment.course.credits for enrollment in self.courseenrollment_set.all() if enrollment.course)
        return total_credits - earned_credits

    def get_advisor(self):
        return self.advisor

class CourseEnrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    enrollment_date = models.DateField(null=True)
    grade = models.CharField(max_length=2, null=True)

class Schedule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    academic_year = models.CharField(max_length=9, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField(Course)

class UploadedDataFile(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True)



class DegreeRequirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    credits_required = models.IntegerField(null=True)
    
    def is_satisfied_by(self, student):
        pass
