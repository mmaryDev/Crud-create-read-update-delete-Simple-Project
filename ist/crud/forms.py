from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']  
        
        labels = {
            'name': 'Name',
            'age': 'Age',
            'email': 'Email',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter age'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }
        
