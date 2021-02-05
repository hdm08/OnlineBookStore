from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'USERNAME'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FIRST NAME'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LAST NAME'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'EMAIL'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'PASSWORD'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'CONFIRM PASSWORD'}))
    class Meta:
        model=User
        fields = ['username', 'email', 'first_name','last_name','password1', 'password2']


class ProfileForm(forms.ModelForm):
    picture = forms.ImageField()
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ADDRESS'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CITY'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'STATE'}))
    pincode = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'PINCODE'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'PHONE'}))
    university_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UNIVERSITY NAME'}))
    class Meta:
        model=models.Profile
        fields = ['picture','address','city','pincode','state','phone','university_name']


class SellBookForm(forms.ModelForm):
    # image = forms.ImageField()
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BOOK NAME'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SUBJECT'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'BOOK PRICE'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DESCRIPTION'}))
    college_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'COLLEGE'}))
    book_university = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UNIVERSITY'}))
    seller_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'OWNER NAME'}))
    seller_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'OWNER E-MAIL'}) )


    class Meta:
        model=models.SellBook
        fields = ['image','name','subject','price','description','college_name','book_university','seller_name','seller_email']






class ContactUsForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    From = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'Your Email'}))
    Subject=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Subject'}))
    Message=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Message'}))
    class Meta:
        model=models.ContactUs
        fields=['username','From','Subject','Message']



x=forms.TextInput(attrs={'class':'form-control'})
class OrderForm(forms.ModelForm):
    name=forms.CharField(widget=x)
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=x)
    state=forms.CharField(widget=x)
    city=forms.CharField(widget=x)
    postal_zip=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model=models.Order
        fields=['name','email','phone','address','state','city','postal_zip']
