from django.shortcuts import render

from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .models import ChangeInput


class HomePageView(TemplateView):
    template_name = 'home.html'


class ResultsView(ListView):
    model = ChangeInput
    template_name = 'results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('digits')
        object_list = ChangeInput.objects.filter(
            Q(numbers__icontains=query) | Q(textOutput__icontains=query)
        )
        return object_list
