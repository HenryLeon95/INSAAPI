from django.shortcuts import render
from django.views.generic import TemplateView


# def HomePageView(request):
#     return render(request, "base.html")
class HomePageView(TemplateView):
    template_name = 'base.html'

class PortfolioPageView(TemplateView):
    template_name = 'pages/portafolio.html'