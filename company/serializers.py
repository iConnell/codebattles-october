from rest_framework.serializers import ModelSerializer
from .models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Company