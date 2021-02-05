from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Profile)
admin.site.register(models.SellBook)
admin.site.register(models.ContactUs)
admin.site.register(models.Order)
