
from django import forms


from django.contrib.auth.models import User
from .models import Personaldetails,allusers,Profile,Content,textbox,Post,Comment
from django.contrib.auth.forms import UserCreationForm
class textboxes(forms.ModelForm):
     post=forms.CharField(
        widget=forms.TextInput(
            attrs= {'placeholder':'Whats there on your mind??','class':'form-control'}
        ))
     class Meta:
          model=Profile
          fields=['post']

class textbox(forms.ModelForm):
     post1=forms.CharField(
        widget=forms.TextInput(
            attrs= {'placeholder':'Whats there on your mind??','class':'form-control'}
        ))
     class Meta:
          model=Profile
          fields=['post1']
class ProfileD(forms.ModelForm):
     username=forms.CharField(
        widget=forms.TextInput(
            attrs= {'placeholder':'Enter your name','class':'form-control'}
        ))
        
     des=forms.CharField(
        widget=forms.TextInput(
            attrs= {'placeholder':'Enter some description about you','class':'form-control'}
        ))
    #  image=forms.ImageField(
    #     widget=forms.ImageField(
    #         attrs= {'placeholder':'Upload your profile picture','class':'form-control'}
    #     ))
        
     age=forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {'placeholder':'Enter your age','class':'form-control'}
        ))
     email=forms.EmailField(
        widget=forms.EmailInput(
            attrs= {'placeholder':'Enter your email','class':'form-control'}
        ))
        
     phone=forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {'placeholder':'Enter your phonenumber','class':'form-control'}
        ))
     class Meta:
          model=Profile
          fields='__all__'

class PersonalD(forms.ModelForm):
     name=forms.CharField(
        widget=forms.TextInput(
            attrs= {'placeholder':'Enter your name','class':'form-control'}
        ))
        
     des=forms.CharField(
        widget=forms.TextInput(
            attrs= {'placeholder':'Enter some description about you','class':'form-control'}
        ))
    #  image=forms.ImageField(
    #     widget=forms.ImageField(
    #         attrs= {'placeholder':'Upload your profile picture','class':'form-control'}
    #     ))
        
     age=forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {'placeholder':'Enter your age','class':'form-control'}
        ))
     email=forms.EmailField(
        widget=forms.EmailInput(
            attrs= {'placeholder':'Enter your email','class':'form-control'}
        ))
        
     phone=forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {'placeholder':'Enter your phonenumber','class':'form-control'}
        ))
     class Meta:
          model=Profile
          exclude=['User','ename']
class alluser(forms.ModelForm):
     class Meta:
          model=allusers
          fields='__all__'

          
class Content(forms.ModelForm):
     
     class Meta:
          model=Content
          fields='__all__'  

class Registerform(UserCreationForm):
        username=forms.CharField(
        widget=forms.TextInput(
            attrs= {'placeholder':'Enter your name','class':'form-control'}
        ))
        
        age=forms.CharField(
        widget=forms.NumberInput(
            attrs= {'placeholder':'Enter your age','class':'form-control'}
        ))
        email=forms.CharField(
        widget=forms.EmailInput(
            attrs= {'placeholder':'Enter your email','class':'form-control'}
        ))
          
        des=forms.CharField(
        widget=forms.TextInput(
            attrs= {'placeholder':'Enter some description about you','class':'form-control'}
        ))
        password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs= {'placeholder':'Enter your password','class':'form-control'}
        ))
        password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs= {'placeholder':'Confirm your password','class':'form-control'}
        ))
       
        class Meta:
          model=User
          fields=["password1","password2","age","email","username"]
class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']