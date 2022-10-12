from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company
from django.urls import reverse

class BaseAdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = [
            'id',
            'name',
            'profile_pic',
            'short_bio'
        ]

class CompanySerializer(ModelSerializer):
    advocates = SerializerMethodField('get_advocates')

    def get_advocates(self, instance):
        query = instance.advocate_set.all()
        advocates = BaseAdvocateSerializer(query, many=True).data
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


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        del data['company']['summary']
        data['company']['href'] = reverse('company-detail', kwargs={'pk': data['company']['id']})
        data['links'] = {
            "youtube": instance.youtube,
            "twitter": instance.twitter,
            "github": instance.github
        }
        return data

    class Meta:
        model = Advocate
        fields = [
            'id',
            'name',
            'profile_pic',
            'short_bio',
            'long_bio',
            'advocate_years_exp',
            'company',
        ]