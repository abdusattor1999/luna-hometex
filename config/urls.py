from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('dashboard/', admin.site.urls, name='dashboard'),
    path('', include("apps.news.urls"), name="news"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns=i18n_patterns(*urlpatterns, prefix_default_language=True)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^contexts/', include('rosetta.urls'))
    ]