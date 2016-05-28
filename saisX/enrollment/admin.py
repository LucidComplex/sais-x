from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Address)
admin.site.register(models.Course)
admin.site.register(models.Institution)
admin.site.register(models.Program)
admin.site.register(models.Student)