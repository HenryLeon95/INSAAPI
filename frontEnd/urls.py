from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
]