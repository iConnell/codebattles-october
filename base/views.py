from rest_framework.viewsets import ModelViewSet
from .serializers import AdvocateSerializer, CompanySerializer
from .models import Advocate, Company
from .pagination import CustomPagination
# Create your views here.

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AdvocateViewSets(ModelViewSet):
    serializer_class = AdvocateSerializer

    def get_queryset(self):
        queryset = Advocate.objects.all()
        name = self.request.query_params.get('query')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset