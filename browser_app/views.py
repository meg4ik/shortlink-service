from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .form import LinkForm

# Create your views here.

class MainView(View):
    def get(self, request):
        context_data = {
            'form' : LinkForm
        }
        return render(request, 'main.html',context_data)

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