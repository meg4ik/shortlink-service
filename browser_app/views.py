from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .form import LinkForm
from django.core.exceptions import ValidationError
from .models import Link, User
from .func import create_shortlink, get_user_ip
from datetime import datetime

# Create your views here.

class MainView(View):
    def get(self, request):
        context_data = {
            'form' : LinkForm
        }
        return render(request, 'main.html',context_data)

    def post(self, request):
        filled_form = LinkForm(request.POST)
        if not filled_form.is_valid():
            raise ValidationError("Link is not valid")

        obj = filled_form.save(commit=False)
        obj.short_link = create_shortlink()
        obj.last_enter_date = datetime.now()
        obj.user_ip = get_user_ip(request)

        if self.request.user.is_authenticated:
            obj.user = self.request.user
        else:
            obj.user = User.objects.get(username='fakeuser')
        obj.save()

        return redirect('main')

class ListView(View):
    def get(self, request):
        return render(request, 'list.html')

class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    next_page = '/'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    next_page = '/'

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)