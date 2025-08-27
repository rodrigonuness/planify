from django.db import models

class Task(models.Model):
    day_of_week = models.CharField(max_length=10)  # ex: 'Monday'
    time = models.TimeField()
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

class Upload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
