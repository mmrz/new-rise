from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import User, Subscriptions
from django.contrib import messages


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=40,)
    password = forms.CharField(label=_("Password"), max_length=40,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("email", "password")


class UserCreationForm(forms.ModelForm):
    email = forms.CharField(label='Email', max_length=40, error_messages=
    {'required': 'پر کردن ایمیل الزامی است.',
     'unique': 'شما قبلا با ایتن ایمیل ثبت نام کرده اید.',
     'invalid': 'آدرس ایمیل خود را صحیح وارد کنید.',})
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    sub = forms.BooleanField(initial=False, required=False)
    rule = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = User
        fields = ("email", "password", "password2", )




    # def clean_name(self):
    #     email = self.cleaned_data['email']
    #     if Users.objects.filter(email=email).exists():
    #         raise forms.ValidationError('The name [%s] already exists' % email)
    #     return email

class UpdateProfile(forms.ModelForm):

    class Meta:
        model = User
        fields = ("gender", "phone", "first_name", "last_name", "birth_date", "cell_phone")


class SubscriptionsForm(forms.ModelForm):
    sub_email = forms.CharField(label='Email', max_length=40, required=False)

    class Meta:
        model = Subscriptions
        fields = ("sub_email", )

