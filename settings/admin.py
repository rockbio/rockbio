from django.contrib import admin
from .models import S3Credential, Provider, SubscriptionHolder

admin.site.register(S3Credential)
admin.site.register(Provider)
admin.site.register(SubscriptionHolder)


