from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf.urls.i18n import i18n_patterns
from decouple import config
from crm.views import assetlinks, privacyPolicy
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="CoreNexus CRM API",
        default_version='v1',
        description="""
        Welcome to the CoreNexus CRM API Documentation.
        CoreNexus is a centralized hub for managing subscriptions, automated lotteries, and community engagement.
        
        Key Modules:
        * 🔑 Membership Lifecycle (Common60/61/70)
        * 🏆 Lottery & Reward Engines
        * 📱 Mobile-First Social Feed (Posts, Stories, Interaction)
        * 🔔 Real-time Firebase Notifications
        """,
        terms_of_service="https://dcm.sjpy.ir/terms/",
        contact=openapi.Contact(email="javadi.dev@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/", include('api.urls', namespace='api')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("i18n/", include("django.conf.urls.i18n")),
    path('.well-known/assetlinks.json', assetlinks),
    path('privacy-policy', privacyPolicy, name='privacyPolicy'),
    # Api Doc
    path('swagger.<format>/',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]

urlpatterns += i18n_patterns(
    path('administrator/programmer/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('crm.urls', namespace='crm')),
)


if config('DEBUG', default=True, cast=bool) == True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# Hide Django rest framework Routers Api View Page Or config in settings.py
# if not DEBUG:
#     REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
#         "rest_framework.renderers.JSONRenderer",
#     )


admin.site.site_header = _('Control Panel')
admin.site.site_title = _('Control Panel')
admin.site.index_title = _('Wellcome to Control Panel')

# handler404 = 'crm.views.handler404'
# handler500 = 'crm.views.handler500'
