from django.shortcuts import render

class JoinView(TemplateView):
    template_name = 'registration/join_form.html'
