from rest_framework.serializers import ModelSerializer
from .models import Advocate, Links

class LinkSerializer(ModelSerializer):
    class Meta:
        model = Links
        fields = [
            'name', 'url'
        ]

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        field = '__all__'