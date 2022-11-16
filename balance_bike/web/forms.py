from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "placeholder": "Потребителско име"
        })
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password", "placeholder": "Парола"
        }),
    )

# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = UserModel
#         fields = ('username', 'first_name', 'last_name', 'email')
#         exclude = ('password',)
#         labels = {
#             'username': 'Username',
#             'first_name': 'First Name',
#             'last_name': 'Last Name',
#             'email': 'Email',
#
#         }
