from django.db import models

# Create your models here.
class Product(models.Model):
    cid = models.CharField(max_length=30)
    pname=models.CharField(max_length=30)
    amt=models.IntegerField()

    def __str__(self):
        return self.pname
    
class Customer(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    email=models.CharField(max_length=25)

    def __str__(self):
        return self.name