from django.db import models

# Create your models here.

class Register(models.Model):
    firstname=models.CharField(max_length=30,null=False, blank=False)
    lastname=models.CharField(max_length=30,null=False, blank=False)
    email=models.CharField(max_length=30,null=False, blank=False)
    password=models.CharField(max_length=30,null=False, blank=False)
    def __str__(self):
        return self.id
    

class Login(models.Model):
    lemail=models.CharField(max_length=30,null=False, blank=False)
    lpassword=models.CharField(max_length=30,null=False, blank=False)
    def __str__(self):
        return self.id