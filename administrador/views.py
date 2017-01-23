from django.shortcuts import render
from django.views.generic import *


# Create your views here.
class AfterLogin(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(
            AfterLogin, self).get_context_data(**kwargs)
        # dropTable(self.request)
        return context
