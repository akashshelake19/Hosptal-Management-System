from django.contrib import admin
from .models import OPD_Reg
# Register your models here.
class OPD_Reg_Admin(admin.ModelAdmin):
    list_display = ['id','name','email','dob','gender','addr','ph_no']

admin.site.register(OPD_Reg,OPD_Reg_Admin)