from django.db import models

# Create your models here.

class ContactModel(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=500, null=False)
    email = models.EmailField(null=False)
    message = models.TextField(max_length=500, null= False)
    
    def __str__(self):
        return self.first_name
