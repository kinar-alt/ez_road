from django.db import models


class Contact_us(models.Model):
    email=models.EmailField()
    address=models.CharField(max_length=100)
    zipCode=models.CharField(max_length=20)
    queries=models.TextField(max_length=1000)

    def __str__(self):
        return self.email
# Create your models here.
