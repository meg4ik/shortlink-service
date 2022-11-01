from django.urls import path

from .views import MainView, LoginInterfaceView, LogoutInterfaceView, SignupView, ListView, RedirectView, DelView

urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path('list', ListView.as_view(), name='list'),
    path('redirect/<str:shortlink>', RedirectView.as_view(), name='redirect'),
    path('list/delete/<int:pk>', DelView.as_view(), name='delete'),

    path('login', LoginInterfaceView.as_view(), name='login'),
    path('logout', LogoutInterfaceView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),

]