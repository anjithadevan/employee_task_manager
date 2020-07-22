from django.contrib import admin
from task_manager import models
# Register your models here.
admin.site.register(models.Task)
admin.site.register(models.Comment)
