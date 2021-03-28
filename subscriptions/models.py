from django.db import models

import uuid

from django.db.models import Sum
from django.conf import settings

# Subscription models:
class Subscription(models.Model):
    subscription_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    age = models.CharField(max_length=3, null=False, blank=False)
    subscription_total = 6.99

    def _generate_subscription_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.subscription_number:
            self.subscription_number = self._generate_subscription_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subscription_number
