import os

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'tracker_development.settings',
)

from django.core.asgi import get_asgi_application

django_asgi_application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path

import tracker.routing

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path(
                    'tracker/',
                    URLRouter(tracker.routing.websocket_urlpatterns),
                )
            ])
        )
    ),
    'http': django_asgi_application,
})