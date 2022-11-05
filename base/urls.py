from django.urls import path
from .views import CompanyViewSet, AdvocateViewSets

urlpatterns = [
    path('companies/', CompanyViewSet.as_view({'get':'list', 'post':'create'}), name='company-list'),
    path('companies/<int:pk>/', CompanyViewSet.as_view({'get':'retrieve'}), name='company-detail'),
    path('advocates/', AdvocateViewSets.as_view({'get':'list', 'post':'create'}), name="advocates-list"),
    path('advocates/<str:username>/', AdvocateViewSets.as_view({'get': 'retrieve'}))
]