from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    path('forms/', views.form_page, name='form_page'),   
    
    # Students
    path("students/", views.StudentListView.as_view(), name="student-list"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student-detail"),
    path('add_student/', views.add_student, name='add_student'),
    path('create-student/', views.create_student, name='create_student'),
    path('update-student/<int:pk>/', views.update_student, name='update_student'),
    path('delete-student/<int:pk>/', views.delete_student, name='delete_student'),
    path('list-students/', views.list_students, name='list_students'),

    # Degree Programs
    path("degree-programs/", views.DegreeProgramListView.as_view(), name="degreeprogram-list"),
    path("degree-programs/<int:pk>/", views.DegreeProgramDetailView.as_view(), name="degreeprogram-detail"),
    path('create-degree-program/', views.create_degree_program, name='create_degree_program'),
    path('update-degree-program/<int:pk>/', views.update_degree_program, name='update_degree_program'),
    path('delete-degree-program/<int:pk>/', views.delete_degree_program, name='delete_degree_program'),
    path('list-degree-programs/', views.list_degree_programs, name='list_degree_programs'),

    # Courses
    path("courses/", views.CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(), name="course-detail"),
    path('add_course/', views.add_course, name='add_course'),
    path('create-course/', views.create_course, name='create_course'),
    path('update-course/<int:pk>/', views.update_course, name='update_course'),
    path('delete-course/<int:pk>/', views.delete_course, name='delete_course'),
    path('list-courses/', views.list_courses, name='list_courses'),

    # Semesters
    path('semesters/', views.SemesterListView.as_view(), name='semester-list'),
    path('semesters/<int:pk>/', views.SemesterDetailView.as_view(), name='semester-detail'),
    path('add_semester/', views.add_semester, name='add_semester'),
    path('create-semester/', views.create_semester, name='create_semester'),
    path('update-semester/<int:pk>/', views.update_semester, name='update_semester'),
    path('delete-semester/<int:pk>/', views.delete_semester, name='delete_semester'),
    path('list-semesters/', views.list_semesters, name='list_semesters'),

    # Advisers
    path("advisers/", views.AdviserListView.as_view(), name="adviser-list"),
    path("advisers/<int:pk>/", views.AdviserDetailView.as_view(), name="adviser-detail"),
    path('create-adviser/', views.create_adviser, name='create_adviser'),
    path('update-adviser/<int:pk>/', views.update_adviser, name='update_adviser'),
    path('delete-adviser/<int:pk>/', views.delete_adviser, name='delete_adviser'),
    path('list-advisers/', views.list_advisers, name='list_advisers'),

    # Degree Requirements
    path("degree-requirements/", views.DegreeRequirementListView.as_view(), name="degreerequirement-list"),
    path("degree-requirements/<int:pk>/", views.DegreeRequirementDetailView.as_view(), name="degreerequirement-detail"),
    path('create-degree-requirement/', views.create_degree_requirement, name='create_degree_requirement'),
    path('update-degree-requirement/<int:pk>/', views.update_degree_requirement, name='update_degree_requirement'),
    path('delete-degree-requirement/<int:pk>/', views.delete_degree_requirement, name='delete_degree_requirement'),
    path('list-degree-requirements/', views.list_degree_requirements, name='list_degree_requirements'),

    # Course Enrollments
    path("course-enrollments/", views.CourseEnrollmentListView.as_view(), name="courseenrollment-list"),
    path("course-enrollments/<int:pk>/", views.CourseEnrollmentDetailView.as_view(), name="courseenrollment-detail"),
    path('create-course-enrollment/', views.create_course_enrollment, name='create_course_enrollment'),
    path('update-course-enrollment/<int:pk>/', views.update_course_enrollment, name='update_course_enrollment'),
    path('delete-course-enrollment/<int:pk>/', views.delete_course_enrollment, name='delete_course_enrollment'),
    path('list-course-enrollments/', views.list_course_enrollments, name='list_course_enrollments'),
]
