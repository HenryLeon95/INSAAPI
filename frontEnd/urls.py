from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('services/', ServicePageView.as_view(), name='services'),
    path('domains_hosting/', Domain_HostingPageView.as_view(), name='domains_hosting'),
    path('terms_conditions/', Terms_ConditionsPageView.as_view(), name='terms_conditions'),
]