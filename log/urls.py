from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workouts', views.index, name='workouts'),
    path('workout/create/', views.WorkoutCreateView.as_view(), name='workout-create'),
]