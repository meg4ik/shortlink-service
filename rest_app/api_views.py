from rest_framework.generics import ListAPIView, CreateAPIView
from rest_app.serializers import LinkSerializer, LinkCreateSerializer
from browser_app.models import Link
from browser_app.func import get_user_ip, create_shortlink, get_fake_user

class LinkList(ListAPIView):
    serializer_class = LinkSerializer
    def get_queryset(self):
        links = Link.objects.filter(user_ip = get_user_ip(self.request)).filter(user = get_fake_user()).filter(is_delete = False)
        return links

class LinkCreate(CreateAPIView):
    serializer_class = LinkCreateSerializer
    def perform_create(self, serializer):
        serializer.save(short_link=create_shortlink(), user_ip=get_user_ip(self.request), user=get_fake_user())
