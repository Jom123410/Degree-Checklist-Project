from django.db import models

# Define the Semester model
class Semester(models.Model):
    name = models.CharField(max_length=100, unique=True)  # To ensure each semester has a unique name.
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

# Define the Student model
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_enrolled_courses(self, semester=None):
        if semester:
            return self.courseenrollment_set.filter(semester=semester)
        return self.courseenrollment_set.all()

    def get_remaining_credits(self):
        total_credits = self.degree_program.total_credits_required
        earned_credits = sum(enrollment.course.credits for enrollment in self.get_enrolled_courses())
        return total_credits - earned_credits

    def get_advisor(self):
        return self.advisor

# Define the DegreeProgram model
class DegreeProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    total_credits_required = models.IntegerField()
    duration_in_years = models.IntegerField()
    program_description = models.TextField()

    def __str__(self):
        return self.program_name

# Define the Course model
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    prerequisites = models.ManyToManyField('self', blank=True)
    semester_offered = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name
    
    def is_prerequisite_satisfied(self, student):
        # TODO: Add logic to check if prerequisites for this course are satisfied by the given student.
        pass

# Define the Adviser model
class Adviser(models.Model):
    adviser_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Define the DegreeRequirement model
class DegreeRequirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    credits_required = models.IntegerField()
    
    def is_satisfied_by(self, student):
        # TODO: to check if the student satisfies this requirement.
        pass

# Define the CourseEnrollment model
class CourseEnrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=2)
    
    SEMESTER_CHOICES = [
        ('Fall', 'Fall'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
    ]
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default='Fall')

    def __str__(self):
        return f"{self.student} enrolled in {self.course} during {self.semester}"
