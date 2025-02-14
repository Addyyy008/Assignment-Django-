from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    account_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.account_number})"

class CustomerSupport(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.employee_id})"
