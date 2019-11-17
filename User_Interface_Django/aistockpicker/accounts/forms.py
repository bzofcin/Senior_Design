from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    is_superuser = forms.IntegerField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

