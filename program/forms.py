from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


# class CreateForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'
#
#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2",)
#
#
# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].widget.attrs["class"] = "form-control"
#         self.fields['password'].widget.attrs['class'] = 'form-control'
#

class Search(forms.Form):
    kind_of_word = forms.CharField()