from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone


# Create your models here.

class Regions(models.Model):
    region_name = models.CharField(max_length=25)

    class Meta:
        db_table = 'regions'

    def __str__(self):
        return f'{self.region_name} ({self.id})'


class Countries(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=40)

    class Meta:
        db_table = 'countries'

    def __str__(self):
        return f'{self.country_name} - {self.country_code}'


class Locations(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'locations'

    def __str__(self):
        return f'{self.city} - {self.state_province}'


class Departments(models.Model):
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.department_name


class Jobs(models.Model):
    job_title = models.CharField(max_length=50)
    min_salary = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    max_salary = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    class Meta:
        db_table = 'jobs'

    def __str__(self):
        return self.job_title

    def bringMinSalary(self):
        return f'R$ {self.min_salary}'

    def bringMaxSalary(self):
        return f'R$ {self.max_salary}'


class Hierarchy(models.Model):
    title = models.CharField(max_length=10)

    class Meta:
        db_table = 'hierarchy'

    def __str__(self):
        return f'{self.title}'


class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField('Hire date')
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    manager_id = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    title = models.ForeignKey(Hierarchy, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def hireDate(self):
        return self.hire_date.strftime('%d/%m/%Y')

    def bringSalary(self):
        return f'R$ {self.salary}'

class Dependents(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=80)
    birth_date = models.DateField('Birth Date')
    active = models.BooleanField(default=True)
    relationship = models.CharField(max_length=25)
    health_plan_number = models.CharField(max_length=12)
    dental_plan = models.CharField(max_length=12)
    life_insurance = models.CharField(max_length=12)

    class Meta:
        db_table = 'dependents'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.relationship}'

    def age(self):
        now = timezone.now()
        birth = self.birth_date
        age = now - birth
        return age.years


class Banks(models.Model):
    bank_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'banks'

    def __str__(self):
        return self.bank_name

class BankInformation(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)
    branch = models.IntegerField(blank=True, null=True)
    branch_digite = models.IntegerField(blank=True, null=True)
    account = models.IntegerField(blank=True, null=True)
    account_digite = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'employees_bank_information'

    def fullBranch(self):
        return f'{self.branch} - {self.branch_digite}'

    def fullAccount(self):
        return f'{self.account} - {self.account_digite}'


class Payments(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField('Payment Date')

    class Meta:
        db_table = 'payments'

    def bringValue(self):
        return f'R$ {self.value}'

    def paymentDate(self):
        return self.payment_date.strftime('%d/%m/%Y')

class EmployeeAddress(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9)
    address = models.CharField(max_length=250)
    complement = models.TextField()
    number = models.IntegerField(blank=False, null=False)
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    reference = models.TextField()
    current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee_address'

        def __str__(self):
            return f'{self.employee_id} address'

class EmployeeBenefits(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    food_voucher = models.DecimalField(max_digits=6, decimal_places=2)
    meal_ticket = models.DecimalField(max_digits=6, decimal_places=2)
    snack_break = models.BooleanField(default=True)
    gympass = models.BooleanField(default=True)
    free_dressing = models.BooleanField(default=True)
    flex_work_hours = models.BooleanField(default=True)
    transportation_vouchers_type = models.CharField(max_length=50)
    transportation_vouchers_value = models.DecimalField(max_digits=6, decimal_places=2)
    health_plan_number = models.CharField(max_length=12)
    dental_plan = models.CharField(max_length=12)
    life_insurance = models.CharField(max_length=12)
    pl = models.BooleanField(default=True)

    class Meta:
        db_table = 'employee_benefits'

    def __str__(self):
        return self.health_plan_number








