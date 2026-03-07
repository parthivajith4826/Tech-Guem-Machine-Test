from django import forms
from .models import Students

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name','email','age']
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if len(name) < 2:
            raise forms.ValidationError("Name must contain atleast 3 words")
        
        for i in name:
            if i.isdigit():
                raise forms.ValidationError("name do not contain digit")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get("email").strip()
        
        return email
    
    def clean_age(self):
        age = self.cleaned_data.get("age")
        return age
        