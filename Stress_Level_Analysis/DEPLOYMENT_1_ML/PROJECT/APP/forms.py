from django import forms 
from . models import UserPredictModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserPredictForm(forms.ModelForm):
    
    class Meta:
        model = UserPredictModel
        fields = '__all__'

