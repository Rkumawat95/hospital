from django import forms
from .models import User

class PetientRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname','lastname','gender','Disease','doctor','doctor_fees','admit_date']
        widgets = {
            'firstname' : forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'First Name'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Last Name'}),
            'gender' : forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Gender'}),
            'Disease' : forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Disease'}),
            'doctor' : forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Doctor Name'}),
            'doctor_fees' : forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Doctor Fees'}),
            'admit_date' : forms.DateInput(attrs={'class':'form-control mt-2','placeholder':'Admit date'}),
        }