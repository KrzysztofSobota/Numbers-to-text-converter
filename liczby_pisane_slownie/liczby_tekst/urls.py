from django.urls import path
from .views import HomePageView, ResultsView

urlpatterns = [
    path('search/', ResultsView.as_view(), name='results'),
    path('', HomePageView.as_view(), name='home'),
]
