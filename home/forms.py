from email.policy import default
from django import forms  
from .models import CustomUser, UserProfile
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm(UserCreationForm): 
    username = forms.CharField(label='Username', min_length=5, max_length=150)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = CustomUser.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = CustomUser.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = CustomUser.objects.create_user(
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']

        ) 
        return user  


    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2','first_name','last_name')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    phone_number = forms.CharField(required=False, max_length=12)

    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','phone_number']