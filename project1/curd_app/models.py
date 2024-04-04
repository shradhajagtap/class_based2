from django.db import models


class Employee(models.Model):
    emp_company_name = models.CharField(max_length=10)
    emp_first_name = models.CharField(max_length=20)
    emp_last_name = models.CharField(max_length=20)
    emp_id = models.IntegerField()
    emp_city = models.CharField(max_length=10)


