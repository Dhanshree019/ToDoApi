from django.db import models

# Create your models here.

class ToDoData(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'todo_table'

