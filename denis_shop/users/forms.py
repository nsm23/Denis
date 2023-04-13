from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from users.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    """Форма профиля юзера"""

    class Meta:
        model = User
        fields = ['username', 'birthday',
                  'email', 'phone', 'avatar']
        widget = {
            'birthday': DateInput,
        }


class UserRegisterForm(forms.ModelForm):
    """Форма регистрации"""

    class Meta:
        model = User
        fields = ('username', 'email')

    password = forms.CharField(label='пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='повторите пароль',
                                widget=forms.PasswordInput)

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class UserForgotPasswordForm(PasswordResetForm):
    """Запрос на восстановление пароля"""

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control',
                 'autocomplete': 'off'}
            )


class UserSetNewPassword(SetPasswordForm):
    """Смена пароля после подтверждения"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control',
                 'autocomplete': 'off'}
            )
