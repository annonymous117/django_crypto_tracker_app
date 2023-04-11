from django import forms
from .models import*
from django.forms import ModelForm
class UserForm(forms.Form):
    name=forms.CharField(label='Enter your names')
    email=forms.CharField(label='Enter email')
    comment=forms.CharField(label='Enter your comment')
class msgForm(forms.Form):
    msgfromemail=forms.CharField(label='Enter from email')
    toemail=forms.CharField(label='Enter destination email')
    message=forms.CharField(label='type in your message')
class userclass(forms.Form):
    names=forms.CharField(label=" Enter your names")
    email=forms.EmailField(label=" Enter user email")
    phone=forms.IntegerField(label=" Enter user number")
    message=forms.CharField(label=" Enter user message")
class Messageform(forms.ModelForm):
    class Meta:
        model=Message
        fields="__all__"
   
class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model=Userfeedback
        fields="__all__"
class UserEmailform(forms.ModelForm):
    class Meta:
        model=Sendmailmsg
        fields="__all__"

