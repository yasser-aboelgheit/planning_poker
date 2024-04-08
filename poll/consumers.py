# import json
# from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(WebsocketConsumer):
#     async def connect(self) :
#         self.group_name = 'notification'
#         # join to group
#         await self.channel_layer.group_add(self.group_name, self.channel_name)

#         await self.accept()
    
#     async def disconnect(self):
#         # leave group
#         await self.channel_layer.group_discard(self.group_name,
#                                                self.channel_name)

#     # Receive message from websocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json[ 'message']
#         event = {
#             'type': 'send_message',
#             'message': message
#         }
#         # send message to group
#         await self.channel_layer.group_send(self.group_name, event)

#     # Receive message from group
#     async def send_message (self, event) :
#         message = event['message']

#         # send message to websocket
#         await self.send(text_data=json.dumps ({'message': message} ))


import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = str(self.scope['path'].replace("/", ""))
        url = self.scope['path']
        print(url)

        print("Sssssss")
        print(self.__dict__)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   

    def receive(self, text_data):
        print("inside receive ")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )

    def chat_message(self, event):
        print("inside chat_message ")
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))
