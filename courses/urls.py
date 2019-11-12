from django.urls import path
from .views import CourseListView,SingleCourseView


app_name = "courses"
urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>/', SingleCourseView.as_view()),
]