from django.db import models
from django.conf import settings
# Create your models here.

class Instructor(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default=None,on_delete=models.CASCADE)
    instructor_description=models.TextField(max_length=1000)
    email_id=models.EmailField()
    zipcode=models.CharField(max_length=10)
    hourly_rate=models.IntegerField()
    location=models.CharField(max_length=200)
    
    def __str__(self):
        return self.email_id