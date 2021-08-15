from django.views.generic import TemplateView, ListView, DetailView
from django.utils.translation import gettext as _

from .models import Reality

class MainMenuView(TemplateView):
    template_name = 'world/main_menu.html'

class RealityDetailView(DetailView):
    model = Reality
    template_name = 'world/reality_list.html'

class RealityListView(ListView):
    model = Reality
    template_name = 'world/reality_detail.html'

class RealityPlayView(TemplateView):
    template_name = 'world/reality_play.html'

class UpdateProfileView(TemplateView):
    template_name = 'world/profile_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Profile Update')
        return context
