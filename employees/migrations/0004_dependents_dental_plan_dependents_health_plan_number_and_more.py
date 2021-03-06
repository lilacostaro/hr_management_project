# Generated by Django 4.0.1 on 2022-01-27 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employeeaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependents',
            name='dental_plan',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dependents',
            name='health_plan_number',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dependents',
            name='life_insurance',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='EmployeeBenefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_voucher', models.DecimalField(decimal_places=2, max_digits=6)),
                ('meal_ticket', models.DecimalField(decimal_places=2, max_digits=6)),
                ('snack_break', models.BooleanField()),
                ('gympass', models.BooleanField()),
                ('free_dressing', models.BooleanField()),
                ('flex_work_hours', models.BooleanField()),
                ('transportation_vouchers_type', models.CharField(max_length=50)),
                ('transportation_vouchers_value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('health_plan_number', models.CharField(max_length=12)),
                ('dental_plan', models.CharField(max_length=12)),
                ('life_insurance', models.CharField(max_length=12)),
                ('pl', models.BooleanField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employees')),
            ],
            options={
                'db_table': 'employee_benefits',
            },
        ),
    ]
