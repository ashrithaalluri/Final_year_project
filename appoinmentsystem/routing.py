# video_chat_project/routing.py

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import appoinmentsystem.routing

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            appoinmentsystem.routing.websocket_urlpatterns
        )
    ),
})
