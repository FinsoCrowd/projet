"""Finso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import view


urlpatterns = [
    url(r'^$', view.home, name="accueil"),
    url(r'^propos', view.propos, name="propos"),
    url(r'^projetbycategorie/(?P<id>\d+)', view.projetbycategorie, name='projetbycategorie'),
    url(r'^admin/', admin.site.urls),
    url(r'^utilisateur/', include('utilisateur.urls')),
    url(r'^projet/', include('projet.urls')),
    url(r'^admin1/', include('administration.urls')),
    url(r'^contribution/', include('contribution.urls', namespace="contribution_projet")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
