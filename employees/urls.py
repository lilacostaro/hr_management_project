from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employeesList, name='employees_list'),
    path('employees/<int:id>/', views.employeeInfo, name='employee_info')
]