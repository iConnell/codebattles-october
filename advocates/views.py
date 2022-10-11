from rest_framework.viewsets import ModelViewSet
from .serializers import AdvocateSerializer
from .models import Advocate
# Create your views here.


class AdvocateViewSets(ModelViewSet):
    serializer_class = AdvocateSerializer
    queryset = Advocate.objects.all()