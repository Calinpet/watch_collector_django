from django.contrib import admin
# add Service to ther import
from .models import Watch, Service

# Register your models here
admin.site.register(Watch)
# register the new Service Model
admin.site.register(Service)
