from django.db import models

# Create your models here.
class Signup(models.Model):
    Name= models.CharField(max_length=200, null=True, blank=True)
    Mail_id= models.EmailField(default='no_mail@null', max_length=300)
    Password= models.CharField(max_length=20, null=True, blank=True)
