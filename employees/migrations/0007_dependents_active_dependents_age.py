# Generated by Django 4.0.1 on 2022-01-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_employeeaddress_complement'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependents',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dependents',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
