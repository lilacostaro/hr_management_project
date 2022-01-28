from DSEmp.employee_details import Employee
from django.contrib import admin
from .models import (Employees,
                     Banks,
                     Countries,
                     Hierarchy,
                     EmployeeAddress,
                     EmployeeBenefits,
                     Departments,
                     Jobs,
                     Dependents,
                     BankInformation,
                     Payments)
# Register your models here.

class EmployeeAddressInline(admin.StackedInline):
    model = EmployeeAddress
    extra = 1

class EmployeesFullInfo(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['cep']}),
        ('Date information', {'fields': ['created_at']}),
    ]
    inlines = [EmployeeAddressInline]

admin.site.register(Employees)
admin.site.register(Banks)
admin.site.register(Countries)
admin.site.register(Hierarchy)
admin.site.register(EmployeeAddress)
admin.site.register(EmployeeBenefits)
admin.site.register(Departments)
admin.site.register(Dependents)
admin.site.register(Jobs)
admin.site.register(BankInformation)
admin.site.register(Payments)
# admin.site.register(EmployeesFullInfo)

