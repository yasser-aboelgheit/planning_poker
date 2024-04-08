import json
import logging
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

logger = logging.getLogger(__name__)

class PollConsumer(WebsocketConsumer):
    usernames = []
    messages = {}

    def connect(self):
        self.room_group_name = str(self.scope['path'].replace("/", ""))
        logger.info(f"Connecting to room group: {self.room_group_name}")
        if not self.room_group_name in self.messages:
            self.messages[self.room_group_name] = {}
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        logger.info("Connection established")

    def receive(self, text_data):
        logger.info("Received message")
        text_data_json = json.loads(text_data)
        vote = text_data_json.get('vote', "")
        username = text_data_json['username']
        logger.info(f"Received vote from {username}: {vote}")
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'vote': vote,
                'username': username
            }
        )

    def poll_message(self, event):
        vote = event['vote']
        username = event['username']
        if username not in self.usernames:
            self.usernames.append(username)
        logger.info(f"Broadcasting message from {username}: {vote}")
        self.messages[self.room_group_name][username] = username + ' voted  ' + vote
        messages = self.messages[self.room_group_name]
        self.send(text_data=json.dumps({
            'message': messages,
            'vote': vote,
            'username': username
        }))
