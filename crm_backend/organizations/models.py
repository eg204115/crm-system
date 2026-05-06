from django.db import models


class Organization(models.Model):
    BASIC = 'BASIC'
    PRO = 'PRO'

    SUBSCRIPTION_CHOICES = [
        (BASIC, 'Basic'),
        (PRO, 'Pro'),
    ]

    name = models.CharField(max_length=255)
    subscription_plan = models.CharField(
        max_length=10,
        choices=SUBSCRIPTION_CHOICES,
        default=BASIC
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name