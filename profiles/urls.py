from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('order_history_table/', views.order_history_table, name='order_history_table'),

]