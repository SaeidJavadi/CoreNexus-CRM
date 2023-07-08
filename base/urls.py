from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version='v1',
        description="Here Is All Our EndPoints",
        terms_of_service="#",
        contact=openapi.Contact(email="s.a.e.i.d@live.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('crm.urls', namespace='crm')),
    path("api/", include('api.urls', namespace='api')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG == True:
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
