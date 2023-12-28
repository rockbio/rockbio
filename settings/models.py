from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField
from django.contrib.auth.models import AbstractUser


class S3Credential(models.Model):
    def get_absolute_url(self):
        return "/settings/"
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=255)
    access_key = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)
    buckets = models.TextField(null=True, blank=True)
    exclude_paths= models.TextField(null=True, blank=True)
    exclude_files = models.TextField(null=True, blank=True)

class Provider(models.Model):
    def get_absolute_url(self):
        return "/settings/"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    config = JSONField()
    def __str__(self):
        return self.name

class Subnet(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=255)
    config = JSONField()
    count = models.IntegerField(null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            primary_key=True,
        )
    params = JSONField()


class SubscriptionHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    subscription = models.ForeignKey(
        'djstripe.Subscription', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Subscription object, if it exists"
    )
    customer = models.ForeignKey(
        'djstripe.Customer', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Customer object, if it exists"
    )    
