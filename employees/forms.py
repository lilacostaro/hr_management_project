from DSEmp.employee_details import Employee
from django import forms

from .models import (Employees,
                     Regions,
                     Countries,
                     Locations,
                     Departments,
                     Jobs,
                     Hierarchy,
                     Dependents,
                     Banks,
                     BankInformation,
                     Payments,
                     EmployeeAddress,
                     EmployeeBenefits)

class AddEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'hire_date',
                  'department',
                  'job',
                  'title',
                  'salary',
                  'manager_id',
                  'active')

class AddRegionForm(forms.ModelForm):

    class Meta:
        model = Regions
        fields = ('id', 'region_name')


class AddCountryForm(forms.ModelForm):

    class Meta:
        model = Countries
        fields = ('region', 'country_code', 'country_name')


class AddLocationForm(forms.ModelForm):

    class Meta:
        model = Locations
        fields = ('country',
                  'street_address',
                  'postal_code',
                  'city',
                  'state_province',
                  'active')


class AddDepartmentForm(forms.ModelForm):

    class Meta:
        model = Departments
        fields = ('location', 'department_name')


class AddJobForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = ('job_title', 'min_salary', 'max_salary')


class AddHierarchyForm(forms.ModelForm):

    class Meta:
        model = Hierarchy
        fields = ('title',)


class AddPersonalInfoForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class AddCompanyInfoForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = ('hire_date', 'department', 'title', 'job', 'salary', 'manager_id', 'active')



class AddDependentForm(forms.ModelForm):

    class Meta:
        model = Dependents
        fields = ('first_name',
                  'last_name',
                  'birth_date',
                  'relationship',
                  'health_plan_number',
                  'dental_plan',
                  'life_insurance',
                  'active')


class AddBankForm(forms.ModelForm):

    class Meta:
        model = Banks
        fields = ('bank_name', 'bank_id')



class AddBankInfoForm(forms.ModelForm):

    class Meta:
        model = BankInformation
        fields = ('bank', 'branch', 'branch_digite', 'account', 'account_digite')


class AddPaymentForm(forms.ModelForm):

    class Meta:
        model = Payments
        fields = ('employee', 'value', 'payment_date')


class AddEmployeeAddressForm(forms.ModelForm):

    class Meta:
        model = EmployeeAddress
        fields = ('address',
                  'number',
                  'complement',
                  'neighborhood',
                  'cep',
                  'city',
                  'state',
                  'country',
                  'reference',
                  'current')


class AddBenefitsForm(forms.ModelForm):

    class Meta:
        model = EmployeeBenefits
        fields = ('food_voucher',
                  'meal_ticket',
                  'transportation_vouchers_type',
                  'transportation_vouchers_value',
                  'health_plan_number',
                  'dental_plan',
                  'life_insurance')


