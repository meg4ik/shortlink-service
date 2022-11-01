from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .form import LinkForm
from django.core.exceptions import ValidationError, PermissionDenied
from .models import Link, RedirectHistory
from .func import create_shortlink, get_user_ip, get_fake_user
from datetime import datetime
from django.db.models import Max, Count
from ip2geotools.databases.noncommercial import DbIpCity

# Create your views here.

class DelView(View):
    def post(self, request, pk):
        link = Link.objects.get(pk=pk)
        if self.request.user.is_authenticated:
            if link.user != self.request.user:
                raise PermissionDenied
        elif get_user_ip(request) != link.user_ip:
            raise PermissionDenied

        link.is_delete = True
        link.save()

        return redirect('list')

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
        if self.request.user.is_authenticated:
            if Link.objects.filter(user = self.request.user).filter(full_link=request.POST["full_link"]):
                raise ValidationError("Link cannot be repeated")
        else:
            if Link.objects.filter(user_ip = get_user_ip(request)).filter(full_link=request.POST["full_link"]):
                raise ValidationError("Link cannot be repeated")

        obj = filled_form.save(commit=False)
        obj.short_link = create_shortlink()
        obj.user_ip = get_user_ip(request)

        if self.request.user.is_authenticated:
            obj.user = self.request.user
        else:
            obj.user = get_fake_user()
        obj.save()

        return redirect('main')

class ListView(View):
    def get(self, request):
        query = Link.objects
        if self.request.user.is_authenticated:
            links = query.filter(user = self.request.user).filter(is_delete = False)
        else:
            links = query.filter(user = get_fake_user()).filter(user_ip = get_user_ip(request)).filter(is_delete = False)
        complex_link = {}
        for link in links:
            most_common_countries = link.link_history.values("country").annotate(count=Count('country')).order_by("-count")
            date_and_ipcounter = [link.link_history.values('enter_user_ip').distinct().count(), link.link_history.aggregate(Max('enter_date')), most_common_countries]
            complex_link[link] = date_and_ipcounter
        context_data = {'link_data':complex_link}
        return render(request, 'list.html', context_data)

class RedirectView(View):
    def get(self, request, shortlink):
        try:
            response = DbIpCity.get(get_user_ip(request), api_key='free')
            user_counrty = response.country
            if user_counrty == "ZZ":
                user_counrty = "localhost"
        except:
            user_counrty = "Unknown"
        curr_link = Link.objects.get(short_link = shortlink)
        history = RedirectHistory(enter_user_ip=get_user_ip(request), enter_date = datetime.now(), country = user_counrty, link = curr_link)
        history.save()
        return redirect(curr_link.full_link)


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