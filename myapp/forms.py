from django import forms
from myapp.models import login
import re

class Reg(forms.ModelForm):
    firstname= forms.CharField(label="FIRSTNAME", widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"FIRSTNAME"}))
    lastname= forms.CharField(label="LASTNAME",widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"LASTNAME"}))
    email= forms.EmailField(label="EMAIL",widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"name@example.com"}))
    phone= forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"MOBILE NUMBER"}), label="PHONE")
    password= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"PASSWORD"}), label="PASSWORD")
    repassword= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"REPASSWORD"}), label="REPASSWORD")
    class Meta:
        model = login
        fields= '__all__'
        #fields=('email','phone')
        #exclude=("password","repassword")
    def clean_firstname(self):
        data = self.cleaned_data["firstname"]
        return data
    
class Login(forms.Form):
    usermail= forms.CharField(label="USER-EMAIL",widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"name@example.com"}))
    password= forms.CharField(label="PASSWORD", widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"strong password",'for':"floatingInput"}))