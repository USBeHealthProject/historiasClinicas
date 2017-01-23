from django.shortcuts import render
from django.views.generic import *


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(
            Index, self).get_context_data(**kwargs)
        # dropTable(self.request)
        return context
