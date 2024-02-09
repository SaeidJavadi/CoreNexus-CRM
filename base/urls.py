from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf.urls.i18n import i18n_patterns
from decouple import config
from crm.views import assetlinks
# from rest_framework import permissions


urlpatterns = [
    path("api/", include('api.urls', namespace='api')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("i18n/", include("django.conf.urls.i18n")),
    path('.well-known/assetlinks.json', assetlinks),
]

urlpatterns += i18n_patterns(
    path('administrator/programmer/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('crm.urls', namespace='crm')),
)


if config('DEBUG', default=True, cast=bool) == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Hide Django rest framework Routers Api View Page Or config in settings.py
# if not DEBUG:
#     REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
#         "rest_framework.renderers.JSONRenderer",
#     )


admin.site.site_header = _('Control Panel')
admin.site.site_title = _('Control Panel')
admin.site.index_title = _('Wellcome to Control Panel')

handler404 = 'crm.views.handler404'
handler500 = 'crm.views.handler500'
