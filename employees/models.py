from django.db import models


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


class Jobs(models.Model):
    job_title = models.CharField(max_length=50)
    min_salary = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    max_salary = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    class Meta:
        db_table = 'jobs'

    def bringMinSalary(self):
        return f'R$ {self.min_salary}'

    def bringMaxSalary(self):
        return f'R$ {self.max_salary}'


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
    relationship = models.CharField(max_length=25)

    class Meta:
        db_table = 'dependents'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.relationship}'


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



