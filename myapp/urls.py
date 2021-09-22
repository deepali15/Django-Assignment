from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('question1/', views.question1, name="question1"),
    path('question2/', views.question2, name="question2"),
    path('question3/', views.question3, name="question3"),
    
]