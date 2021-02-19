from django import forms
from .models import Signup,Infomation
from django.core import validators
import re

class Signupform(forms.ModelForm):
    class Meta:
        model=Signup
        fields=['name','email','phone_No','d_o_b','password','con_password']
        

        
        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full Name','autofocus':'Ture'}),
        
        
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),

        'phone_No':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phonr No.'}),

        'd_o_b':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter D-O-M.','type':'date'}),

        'password':forms.PasswordInput( render_value=True, attrs={'class':'form-control','placeholder':'Enter Password'}),
        'con_password':forms.PasswordInput( render_value=True, attrs={'class':'form-control ','placeholder':'Password(again)'})
        }
        error_messages={'name':{'required':'Enter Name'},
        
        'email':{'required':'Enter Email'},
        'phone_No':{'required':'Enter Phone No.'},
        'd_o_b':{'required':'Enter D-O-B'},
        'password':{'required':'Enter Password'},
        
        'con_password':{'required':'Password(again)'}}
    
    def clean_name(self):
        valpass = self.cleaned_data["name"]
         
        if len(valpass)<2:
            raise forms.ValidationError('Enter name more then 2 character!')
        if len(valpass)>25:
            raise forms.ValidationError('Enter Name not more then 25 character!')
        
    def clean_email(self):
        valpass = self.cleaned_data["email"]
         
        
        if len(valpass)>50:
            raise forms.ValidationError('Enter Name not more then 50 character!')
        
        
        return valpass
    
    
    def clean_password(self):
        valpass = self.cleaned_data["password"]
         
        if len(valpass)<8:
            raise forms.ValidationError('Enter password more then 8 character!')
        if not re.match(r'^[A-Za-z0-9]+$',valpass):
            raise forms.ValidationError("Password should be a combination of Alphabets and Number.")
       
        
        return valpass
    def clean_con_password(self):
        valpassag = self.cleaned_data["con_password"]
        if len(valpassag)<8:
            raise forms.ValidationError('Enter password more then 4 char')
        if not re.match(r'^[A-Za-z0-9]+$',valpassag):
            raise forms.ValidationError("Password should be a combination of Alphabets and Number.")
        
        return valpassag
    def clean_phone_No(self):
        valpassag = self.cleaned_data["phone_No"]
        if len(valpassag)<10:
            raise forms.ValidationError('Enter password more then 4 char')
        if not re.match(r'^[0-9]+$',valpassag):
            raise forms.ValidationError("Please Enter Number.")
        
        return valpassag

    

    
class Loginform(forms.Form):
    
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','autofocus':'Ture','placeholder':'Enter Email'}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
class Infomationform(forms.ModelForm):
    class Meta:
        model=Infomation
        fields=['remark']
        widgets={'remark':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Remark','autofocus':'Ture'}),
        # 'email':forms.EmailInput(attrs={'class':'form-control','readonly':'Ture'}),
}
     