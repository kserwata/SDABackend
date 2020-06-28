"""zajecia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from authentication.views import index_page, language_changes
from .api import router
from django.views.i18n import JavaScriptCatalog
from django.utils import timezone
from django.views.decorators.http import last_modified

last_modified_date = timezone.now()

urlpatterns = [
    path('jsi18n/',
         last_modified(lambda req, **kw: last_modified_date)(JavaScriptCatalog.as_view()),
         name='javascript-catalog'),
    path('', index_page, name="auth_index_view"),
    path('lang_choose', language_changes, name='language_changes'),
    path('admin/', admin.site.urls),
    path('fleet/', include('fleet.urls')),
    path('authentication/', include('authentication.urls')),
    path('api/', include(router.urls))
]
