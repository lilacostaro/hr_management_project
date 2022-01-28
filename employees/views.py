from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import (Countries,
                     Regions,
                     Employees,
                     EmployeeAddress,
                     EmployeeBenefits,
                     Departments,
                     Jobs,
                     Hierarchy
                     )

# Create your views here.
def index(request):
    countries_list = Countries.objects.all()
    regions_list = Regions.objects.all()
    context = {
        'countries_list': countries_list,
        'regions_list': regions_list
    }
    return render(request, 'employees/index.html', context)

def employeesList(request):
    employees_list = Employees.objects.order_by('first_name')
    context = {'employees_list': employees_list}
    return render(request, 'employees/employees_list.html', context)

def employeeInfo(request, id):
    employee = get_object_or_404(Employees, pk=id)
    def manager_def():
        if employee.manager_id == None:
            manager_id = 100
            return manager_id
        else:
            manager_id = employee.manager_id
            return manager_id
    address = EmployeeAddress.objects.filter(employee_id=id).values('cep',
                                                                    'address',
                                                                    'complement',
                                                                    'number',
                                                                    'neighborhood',
                                                                    'city',
                                                                    'state',
                                                                    'country',
                                                                    'reference',
                                                                    'current')
    benefits = EmployeeBenefits.objects.filter(employee_id=id).values('food_voucher',
                                                                      'meal_ticket',
                                                                      'snack_break',
                                                                      'gympass',
                                                                      'free_dressing',
                                                                      'flex_work_hours',
                                                                      'transportation_vouchers_type',
                                                                      'transportation_vouchers_value',
                                                                      'health_plan_number',
                                                                      'dental_plan',
                                                                      'life_insurance',
                                                                      'pl'
)
    manager = get_object_or_404(Employees, id=manager_def())
    department_id = employee.department_id
    department = get_object_or_404(Departments, id=department_id)
    job_id = employee.job_id
    job = get_object_or_404(Jobs, id=job_id)
    title_id = employee.title_id
    title = get_object_or_404(Hierarchy, id=title_id)
    context = {
        'employee': employee,
        'manager': manager,
        'department': department,
        'job': job,
        'title': title,
        'address': address,
        'benefits': benefits
        }

    return render(request, 'employees/employee_details.html', context)
