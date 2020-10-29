from django.views.generic import TemplateView
from django.shortcuts import redirect

class JoinView(TemplateView):
    template_name = 'registration/join_form.html'
