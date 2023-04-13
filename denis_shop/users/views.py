from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm

# Create your views here.


class UserLoginView(LoginView):
    """Логин"""
    template_name = 'users/user_login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('main')


class UserLogoutView(LogoutView):
    """Лог аут"""
    http_method_names = 'get'
    template_name = '/'
    extra_context = None


def registration(request):
    if request.method == 'POST':
        registration_form = UserRegisterForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.set_password(registration_form.cleaned_data['password'])
            user.save()
            return render(request,
                          template_name='users/user_reg_done.html',
                          context={'user': user})
    else:
        registration_form = UserRegisterForm()
    return render(request,
                  template_name='users/user_register.html',
                  context={"reg_form": registration_form})
