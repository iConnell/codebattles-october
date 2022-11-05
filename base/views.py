from rest_framework.viewsets import ModelViewSet
from .serializers import AdvocateSerializer, CompanySerializer
from .models import Advocate, Company
from .pagination import AdvocatePagination, CompanyPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.




@api_view(['GET'])
def base_url(request, format=None):
    return Response({
        'advocates_list': reverse('advocates-list', request=request, format=format),
        'advocate_detail': reverse('advocates-detail', request=request, format=format, kwargs={'username':'dennisivy11'})
    })


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CompanyPagination

class AdvocateViewSets(ModelViewSet):
    serializer_class = AdvocateSerializer
    pagination_class = AdvocatePagination
    lookup_field = 'username'

    def get_queryset(self):
        queryset = Advocate.objects.all()
        name = self.request.query_params.get('query')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset