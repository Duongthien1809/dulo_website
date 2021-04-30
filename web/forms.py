from django import forms
import re
from django.contrib.auth.models import User
from .models import PostModel


class RegisterForm(forms.Form):
        username = forms.CharField(label='Benutzername', max_length=30)
        email = forms.EmailField(label='Email')
        password = forms.CharField(label='Password:', widget=forms.PasswordInput())
        password_repeat = forms.CharField(label='Password wiederholen', widget=forms.PasswordInput())
        first_name = forms.CharField()
        last_name = forms.CharField()
        def clean_password_repeat(self):
            if 'password' in self.cleaned_data:
                password = self.cleaned_data['password']
                password_repeat = self.cleaned_data['password_repeat']
                if password == password_repeat and password:
                    return password_repeat
            raise forms.ValidationError("Password ist nicht idendtisch")

        def clean_username(self):
            username = self.cleaned_data['username']
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError("der Username existiert schon")

        def save(self):
            user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'])
class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label="username eintragen")
    password = forms.CharField(min_length=6, max_length=50, label="Password eintragen", widget=forms.PasswordInput)

class PostModelForm(forms.ModelForm):
        class Meta:
            model = PostModel
            fields = ('title', 'beschreibung', 'preis', 'image')
            labels = {
                'title': 'Deine Titel',
                'Beschreibung': 'schreiben Sie eine Beschreibung über den Artikel!',
                'Preis': 'Preis',
            }