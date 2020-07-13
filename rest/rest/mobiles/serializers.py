from rest_framework import serializers
from .models import Mobile


class MobileDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Mobile
        fields = '__all__'


class MobileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('brand', 'model')
