from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company

class CompanySerializer(ModelSerializer):
    class Meta:
        fields = [
            'id',
            'name',
            'logo',
            'summary',
        ]
        model = Company

class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()

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
            'links',
        ]