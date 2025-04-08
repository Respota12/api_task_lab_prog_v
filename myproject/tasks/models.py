from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    description_service = models.TextField(blank=False, null=True)
    def __str__(self):
        return self.name
        
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="tasks")
    

    def __str__(self):
        return self.title


   
   

