from django.urls import path
from .views import CompanyViewSet, AdvocateViewSets

urlpatterns = [
    path('company/', CompanyViewSet.as_view({'get':'list'}), name='company-list'),
    path('company/<int:pk>/', CompanyViewSet.as_view({'get':'retrieve'}), name='company-detail'),
    path('advocates/', AdvocateViewSets.as_view({'get':'list'}), name="advocates-list"),
    path('advocates/<int:pk>/', AdvocateViewSets.as_view({'get': 'retrieve'}))
]