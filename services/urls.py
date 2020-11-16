from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('<int:service_id>', views.quizz, name='quizz'),
    path('add/', views.add_quizz, name='add_quizz'),
    path('edit/<int:service_id>/', views.edit_quizz, name='edit_quizz'),
    path('delete/<int:service_id>/', views.delete_quizz, name='delete_quizz'),

]