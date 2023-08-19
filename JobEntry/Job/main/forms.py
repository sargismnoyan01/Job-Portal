from django import forms
from .models import JobCreate,Apply,Testimonial,Talent,MessageModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateForm(forms.ModelForm):
    class Meta:
        model=JobCreate
        fields='__all__'

class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','portfolio','coverlatter','img']

class TestForm(forms.ModelForm):
    class Meta:
        model=Testimonial
        fields='__all__'

class TalentForm(forms.ModelForm):
    class Meta:
        model=Talent
        fields='__all__'

class MessageForm(forms.ModelForm):
    class Meta:
        model=MessageModel
        fields='__all__'

class CretionUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','username','last_name','email','password1','password2']