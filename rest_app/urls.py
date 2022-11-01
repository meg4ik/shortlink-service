from django.urls import path
from .api_views import LinkList, LinkCreate

urlpatterns = [
    path('links/', LinkList.as_view(), name="rest_links"),
    path('links/create/', LinkCreate.as_view(), name="rest_create"),
]