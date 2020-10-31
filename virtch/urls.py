"""virtch URL Configuration"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.views.generic.base import RedirectView
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from authentication.views import JoinView
from . import views as base_views

urlpatterns = i18n_patterns(
    path('', include('world.urls'), name='world'),
    path('about/', base_views.AboutView.as_view(), name='about'),
    path('contact/', base_views.ContactView.as_view(), name='contact'),
    path('privacy/', base_views.PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('terms/', base_views.TermsOfUseView.as_view(), name='terms-of-use'),
    path('auth/', include('authentication.urls'), name='auth'),

    # short urls
    path('join/', JoinView.as_view(), name='join'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls, name='admin'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
)

urlpatterns += [
    path('favicon.ico',
        RedirectView.as_view(url='/static/favicon/favicon.ico', permanent=True)
    ),
    path('robots.txt',
        lambda x: HttpResponse('Host: {}\n'.format(settings.SITE_HOSTNAME), content_type='text/plain')
    ),
]

if settings.DEBUG:

    # Serve static files in dev to test without "collectstatic"
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    #from django.conf.urls import static
    #urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Test error pages in dev
    from django.views.generic import TemplateView
    from django.views import defaults as default_views
    from django.http import Http404
    urlpatterns += i18n_patterns(
        path('400/', TemplateView.as_view(template_name='400.html')),
        path('403/', TemplateView.as_view(template_name='403.html')),
        path('404/', default_views.page_not_found, {'exception': Http404()}),
        path('500/', default_views.server_error),
    )
