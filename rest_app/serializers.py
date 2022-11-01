from dataclasses import field
from rest_framework import serializers
from django.db.models import Max, Count

from browser_app.models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['full_link', 'short_link']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["number_of_transitions"] = instance.link_history.values('enter_user_ip').distinct().count()
        data["last_transitions_time"] = instance.link_history.aggregate(Max('enter_date'))
        data["most_common_country"] = instance.link_history.values("country").annotate(count=Count('country')).order_by("-count")
        return data

class LinkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['full_link']