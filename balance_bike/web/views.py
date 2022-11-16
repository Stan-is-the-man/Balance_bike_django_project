from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from balance_bike.web.forms import UserCreateForm, UserLoginForm

UserModel = get_user_model()


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class UserSignUpView(CreateView):
    template_name = 'user-signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'user-login.html'
    form_class = UserLoginForm
    next_page = reverse_lazy('index')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


# class UserEditView(UpdateView):
#     model = UserModel
#     template_name = 'user-edit.html'
#     form_class = UserEditForm
#
#     def get_success_url(self):
#         return reverse_lazy('index')
#     #     return reverse_lazy('details user', kwargs={'pk': self.object.pk})
