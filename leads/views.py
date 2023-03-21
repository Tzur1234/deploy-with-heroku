from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
# Create your views here.

class LeadListView(TemplateView):
    template_name = 'leads/lead-list.html'