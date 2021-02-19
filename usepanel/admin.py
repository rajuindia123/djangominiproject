from django.contrib import admin
from .models import Signup,Infomation
# Register your models here.
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone_No','d_o_b','password','con_password']

@admin.register(Infomation)
class Infomationadmin(admin.ModelAdmin):
    list_display=['id','remark','email']

