from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    # Student URLs
    path("students/", views.StudentListView.as_view(), name="student-list"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student-detail"),
    path('add_student/', views.add_student, name='add_student'),
    
    # DegreeProgram URLs
    path("degree-programs/", views.DegreeProgramListView.as_view(), name="degreeprogram-list"),
    path("degree-programs/<int:pk>/", views.DegreeProgramDetailView.as_view(), name="degreeprogram-detail"),
    
    # Course URLs
    path("courses/", views.CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(), name="course-detail"),
    path('add_course/', views.add_course, name='add_course'),
    
    # Semester URLs
    path('semesters/', views.SemesterListView.as_view(), name='semester-list'),  # Added this line
    path('semesters/<int:pk>/', views.SemesterDetailView.as_view(), name='semester-detail'),
    path('add_semester/', views.add_semester, name='add_semester'),

    # Adviser URLs
    path("advisers/", views.AdviserListView.as_view(), name="adviser-list"),
    path("advisers/<int:pk>/", views.AdviserDetailView.as_view(), name="adviser-detail"),
    
    # DegreeRequirement URLs
    path("degree-requirements/", views.DegreeRequirementListView.as_view(), name="degreerequirement-list"),
    path("degree-requirements/<int:pk>/", views.DegreeRequirementDetailView.as_view(), name="degreerequirement-detail"),
    
    # CourseEnrollment URLs
    path("course-enrollments/", views.CourseEnrollmentListView.as_view(), name="courseenrollment-list"),
    path("course-enrollments/<int:pk>/", views.CourseEnrollmentDetailView.as_view(), name="courseenrollment-detail"),
]
