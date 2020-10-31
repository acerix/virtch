from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'virtch/about.html'

class ContactView(TemplateView):
    template_name = 'virtch/contact.html'

class JoinView(TemplateView):
    template_name = 'registration/join_form.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'virtch/privacy_policy.html'

class TermsOfUseView(TemplateView):
    template_name = 'virtch/terms_of_use.html'
