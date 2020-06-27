from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_video),
    path('quiz/', views.display_video_quiz),
]