from django.contrib import admin
from .models import Subscriber, Service, Subscription, Bill

admin.site.register(Subscriber)
admin.site.register(Service)
admin.site.register(Subscription)
admin.site.register(Bill)
