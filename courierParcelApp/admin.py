from django.contrib import admin

from .models import Merchants, Order

admin.site.register(Merchants)
admin.site.register(Order)
