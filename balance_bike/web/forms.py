from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm, \
    PasswordChangeForm, ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from balance_bike.web.models import Address

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    error_messages = {
        "password_mismatch": _("Паролите не съвпадат. Моля опитайте отново."),
    }
    username = forms.CharField(
        label=_('Потребителско име'),
        strip=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Моля въведете потребителското си име тук"
        })
    )

    email = forms.CharField(
        label=_('Имейл'),
        strip=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Моля въведете имейл за връзка тук"
        })
    )

    password1 = forms.CharField(
        label=_('Парола'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password",
                   'placeholder': 'Моля въведете вашата парола'
                   }
        ),
    )
    password2 = forms.CharField(
        label=_("Потвърждение на паролата"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                   'placeholder': 'Моля потвърдете вашата парола'}))

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2', ]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Потребителско име'),
        strip=False,
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "placeholder": "Моля въведете потребителското си име"
        })
    )
    password = forms.CharField(
        label=_('Парола'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "placeholder": "Моля въведете вашата парола"
        }
        ),
    )


class UserEditForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Потребителска парола"),
        help_text=_(
            "За промяна на паролата Ви, "
            "моля ползвайте менюто Моя Акаунт -> СМЕНИ ПАРОЛА"

        ),
    )

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'phone']
        field_classes = {'username': UsernameField}


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street', 'first_name', 'last_name', 'phone', 'name_for_engraving']

        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Град/Село'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Улица(квартал), номер, вход'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Име на получателя'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Фамилия на получателя'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'За телефонен номер въведете точно 10 цифри'}),
            'name_for_engraving': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'МОЛЯ ВЪВЕДЕТЕ ИМЕ/НА ЗА ГРАВИРАНЕ (МАКС. 20 СИМВОЛА)'}),

        }


class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street', 'first_name', 'last_name', 'phone', 'name_for_engraving']


class PasswordChanging(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Настояща парола"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'auto-focus': True, 'class': 'form-control',
                   'placeholder': 'Моля въведете текущата си парола'}))

    new_password1 = forms.CharField(
        label=_("Нова парола"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control',
                   'placeholder': 'Моля въведете нова парола'}),
        help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(
        label=_("Потвърди новата парола"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control',
                   'placeholder': 'Моля потвърдете новата парола'}))
