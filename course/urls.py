from django.urls import path
from .views import *

app_name = 'course'

urlpatterns = [
    path('createcourse/', CourseList.as_view()),
    path('<int:pk>/', CourseDetail.as_view()),
    path('<int:pk>/update/', CourseDetail.as_view(), name='course-update'),
    path('<int:pk>/destroy/', CourseDetail.as_view(), name='course-destroy'),
    path('<int:pk>/plans/', PlanList.as_view(), name='course-plans'),
    path('<int:pk>/plans/<int:day>/', PlanDetail.as_view(), name='daily-plans')
]