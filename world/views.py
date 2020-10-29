from django.views.generic import TemplateView

class MainMenuView(TemplateView):
    template_name = 'world/main_menu.html'

class WorldDetailView(TemplateView):
    template_name = 'world/world_detail.html'

class WorldPlayView(TemplateView):
    template_name = 'world/world_play.html'
