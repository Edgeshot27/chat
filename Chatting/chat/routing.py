# routing.py
from django.urls import re_path
from . import consumer


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<sender_id>[0-9]+)/(?P<receiver_id>[0-9]+)/$', consumer.ChatConsumer.as_asgi()),
]