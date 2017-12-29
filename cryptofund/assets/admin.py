from django.contrib import admin

from .models import Client, DollarDeposit, Currency, Asset

admin.site.register(Client)
admin.site.register(DollarDeposit)
admin.site.register(Currency)
admin.site.register(Asset)