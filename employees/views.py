from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader

from .forms import (AddEmployeeForm,
                    AddEmployeeAddressForm)

from .models import (Countries,
                     Regions,
                     Employees,
                     EmployeeAddress,
                     EmployeeBenefits,
                     Departments,
                     Jobs,
                     Hierarchy,
                     Dependents,
                     BankInformation,
                     Banks
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
            manager_id = id
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
                                                                    'current'
                                                                    )
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
    dependents = Dependents.objects.filter(employee_id=id).values('first_name',
                                                                  'last_name',
                                                                  'birth_date',
                                                                  'active',
                                                                  'relationship',
                                                                  'health_plan_number',
                                                                  'dental_plan',
                                                                  'life_insurance'
                                                                  )
    bank_info = BankInformation.objects.filter(employee_id=id).values('bank',
                                                                      'branch',
                                                                      'branch_digite',
                                                                      'account',
                                                                      'account_digite',
                                                                      'bank_id')

    #def bankID():
        #if bank_info[0]['bank_id'] is None:
            #bank_id = 0
            #return bank_id
        #else:
            #bank_id = bank_info[0]['bank_id']
            #return bank_id

    manager = get_object_or_404(Employees, id=manager_def())
    department_id = employee.department_id
    department = get_object_or_404(Departments, id=department_id)
    job_id = employee.job_id
    job = get_object_or_404(Jobs, id=job_id)
    title_id = employee.title_id
    title = get_object_or_404(Hierarchy, id=title_id)

    #bank = Banks.objects.filter(id=bankID()).values('bank_name', 'bank_id')
    context = {
        'employee': employee,
        'manager': manager,
        'department': department,
        'job': job,
        'title': title,
        'address': address,
        'benefits': benefits,
        'dependents': dependents,
        'bank_info': bank_info,
        #'bank': bank
        }

    return render(request, 'employees/employee_details.html', context)

def addEmployee(request):
    if request.method == 'POST':
        form1 = AddEmployeeForm(request.POST)

        if form1.is_valid():
            form1.save()
            return redirect('/employees')
    else:
        form1 = AddEmployeeForm()
        return render(request, 'employees/add_employee.html', {'form1': form1})


def addEmployeeAddress(request, id):
    employee = get_object_or_404(Employees, pk=id)
    employee_id = employee.id
    if request.method == 'POST':
        form = AddEmployeeAddressForm(request.POST)

        if form.is_valid():
            address = form.save(commit=False)
            address.employee_id = employee_id
            address.save()
            return redirect('/employees')
    else:
        form = AddEmployeeAddressForm()
        return render(request, 'employees/forms/address.html', {'form': form, 'employee': employee})

def editPersonalData(request, id):
    pass



