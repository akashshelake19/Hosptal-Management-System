from django.db import models

# Create your models here.
class OPD_Reg(models.Model):
    name=models.CharField(max_length=30,null=False)
    email=models.EmailField(max_length=30,null=False)
    dob=models.DateField(null=False)
    gender=models.CharField(max_length=7,null=False)
    addr=models.CharField(max_length=70,null=False)
    ph_no=models.CharField(max_length=13,null=False)
