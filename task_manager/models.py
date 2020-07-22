from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.


class Task(models.Model):
    NEW = 'NEW'
    INPROGRESS = 'IP'
    COMPLETED = 'CT'
    HOLD = 'HD'
    STATUS_OF_TASKS = [(NEW, 'New'), (INPROGRESS, 'In progress'), (COMPLETED, 'Completed'), (HOLD, 'Hold')]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_OF_TASKS, default=NEW)


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)