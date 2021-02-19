from django.db import models

# Create your models here.
class Signup(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    
    email=models.EmailField(max_length=30)
    phone_No=models.CharField(max_length=15)
    d_o_b=models.DateField(auto_now=False,auto_now_add=False)
    password=models.CharField(max_length=70)
    con_password=models.CharField(max_length=70)

class Infomation(models.Model):
    id=models.AutoField(primary_key=True)
    remark=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)

    