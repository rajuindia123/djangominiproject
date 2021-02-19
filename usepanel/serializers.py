from rest_framework import serializers
from .models import Infomation
class StudentCurd(serializers.ModelSerializer):
    class Meta:
        model=Infomation
        fields=['id','remark','email']
        