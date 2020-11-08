from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('<int:service_id>', views.quizz, name='quizz'),

]