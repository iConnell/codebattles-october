from .views import AdvocateViewSets
from django.urls import path


urlpatterns = [
    path('', AdvocateViewSets.as_view({'get':'list'}), name="advocates-list"),
    path('<int:pk>/', AdvocateViewSets.as_view({'get': 'retrieve'}))
]