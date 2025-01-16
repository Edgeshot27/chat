# consumer.py
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from django.contrib.auth import get_user_model



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        sender_id = self.scope["url_route"]["kwargs"]["sender_id"]
        receiver_id = self.scope["url_route"]["kwargs"]["receiver_id"]
        self.room_name = f"chat_user_{min(sender_id, receiver_id)}_to_{max(sender_id, receiver_id)}"
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming WebSocket messages
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_id = self.scope["url_route"]["kwargs"]["sender_id"]
        receiver_id = self.scope["url_route"]["kwargs"]["receiver_id"]

        # Save the message in the database
        User = get_user_model()
        sender = await sync_to_async(User.objects.get,thread_sensitive=False)(id=sender_id)
        receiver = await sync_to_async(User.objects.get,thread_sensitive=False)(id=receiver_id)
        from .models import Message
        await sync_to_async(Message.objects.create, thread_sensitive=False)(
            sender=sender,
            receiver=receiver,
            message=message,
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': sender.username,
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send the message to WebSocket
        message = event["message"]
        await self.send(text_data=json.dumps({
            "message": message,
        }))

