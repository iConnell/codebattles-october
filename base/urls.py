from django.urls import path, include
from .views import CompanyViewSet, AdvocateViewSets, base_url


urlpatterns = [
    path('', base_url, name="root"),
    # path('companies/<int:pk>/', CompanyViewSet.as_view({'get':'retrieve'}), name='company-detail'),
    # path('companies/', CompanyViewSet.as_view({'get':'list', 'post':'create'}), name='company-list'),
    path('advocates/', AdvocateViewSets.as_view({'get':'list', 'post':'create'}), name="advocates-list"),
    path('advocates/<str:username>/', AdvocateViewSets.as_view({'get': 'retrieve'}), name="advocates-detail")
]