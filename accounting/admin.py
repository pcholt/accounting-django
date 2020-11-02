from django.contrib import admin
from .models import Account, Transaction, Clearance

# Register your models here.
admin.site.register([Account, Transaction, Clearance])