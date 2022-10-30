from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company
from django.urls import reverse


class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = [
            'id',
            'name',
            'username',
            'profile_pic',
            'bio',
            'twitter'
        ]


class CompanySerializer(ModelSerializer):
    advocates = SerializerMethodField('get_advocates')

    def get_advocates(self, instance) -> list:
        query = instance.advocate_set.all()
        advocates = AdvocateSerializer(query, many=True).data
        return advocates

    class Meta:
        fields = [
            'id',
            'name',
            'logo',
            'summary',
            'advocates'
        ]
        model = Company

