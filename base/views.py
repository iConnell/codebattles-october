from rest_framework.viewsets import ModelViewSet
from .serializers import AdvocateSerializer, CompanySerializer
from .models import Advocate, Company
# Create your views here.

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AdvocateViewSets(ModelViewSet):
    serializer_class = AdvocateSerializer
    queryset = Advocate.objects.all()