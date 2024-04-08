from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/poll/', consumers.PollConsumer.as_asgi())
    path(r"ws/poll/<str:user_id>/", consumers.PollConsumer.as_asgi())
]
