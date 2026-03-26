from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from auditlog.registry import auditlog

class Organization(models.Model):
    PLAN_CHOICES = [
        ('BASIC', 'Basic'),
        ('PRO', 'Pro'),
    ]

    name = models.CharField(max_length=255)
    subscription_plan = models.CharField(max_length=10, choices=PLAN_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
auditlog.register(Organization)  
    
class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('STAFF', 'Staff'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='users'
        # null=True,
        # blank=True
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
    
auditlog.register(User)


class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='companies'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)  # soft delete

    def __str__(self):
        return self.name
    
auditlog.register(Company)
   
class Contact(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='contacts'
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='contacts'
    )

    full_name = models.CharField(max_length=255)
    email = models.EmailField()

    phone_validator = RegexValidator(
        regex=r'^\d{8,15}$',
        message="Phone must be 8-15 digits"
    )
    phone = models.CharField(
        validators=[phone_validator],
        max_length=15,
        null=True,
        blank=True
    )

    role = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('email', 'company')  # IMPORTANT validation

    def __str__(self):
        return self.full_name
    
auditlog.register(Contact)