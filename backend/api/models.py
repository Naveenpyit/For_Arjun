from django.db import models

class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    priority = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = 'task'