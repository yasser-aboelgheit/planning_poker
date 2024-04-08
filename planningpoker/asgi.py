# """
# ASGI config for planningpoker project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planningpoker.settings')

# application = get_asgi_application()


# import os
# import poll.routing

# from channels.auth import AuthMiddleware
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planningpoker.settings')

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': 
#         URLRouter(
#             poll.routing.websocket_urlpatterns
#         )
    
# })



import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import poll.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planningpoker.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            poll.routing.websocket_urlpatterns
        )
    )
})
