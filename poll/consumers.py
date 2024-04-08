import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    usernames = []
    messages = {}
    def connect(self):
        print(self.scope['path'])
        self.room_group_name = str(self.scope['path'].replace("/", ""))
        url = self.scope['path']
        if not self.room_group_name in self.messages:
            self.messages[self.room_group_name] = {}

        print(url)

        print("Sssssss")
        print(self.room_group_name)
        print(self.channel_name)
        print(self.__dict__)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   

    def receive(self, text_data):
        print("inside receive ")
        text_data_json = json.loads(text_data)
        vote = text_data_json.get('vote', "")
        username = text_data_json['username']
        print(username)
        print(vote)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'vote':vote,
                'username': username
            }
        )

    def chat_message(self, event):
        
        print("inside chat_message ")
        print(self.room_group_name)
        vote = event['vote']
        username = event['username']
        if username not in self.usernames:
            self.usernames.append(username)
        print(self.usernames)
        print()
        self.messages[self.room_group_name][username] = username + ' voted ' + vote
        messages = self.messages[self.room_group_name]
        self.send(text_data=json.dumps({
            'type':'chat',
            'message': list(messages.values()),
            'vote': vote,
            'username': username
        }))
