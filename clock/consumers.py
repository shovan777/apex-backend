import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timezone import localtime, now
from rest_framework_simplejwt.authentication import JWTAuthentication


class ClockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = self.scope["url_route"]["kwargs"]["room_name"]
        # self.room
        # self.room_group_name = "exam_5"
        # self.room_group_name = self.room_name

        # Join clock room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "check_clock",
                "message": "hello",
            },
        )

    async def disconnect(self, close_code):
        # Leave clock room
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        # message = "Hello my friend"
        if "message" in text_data_json:
            message = text_data_json["message"]
            # Send message to clock room
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "check_clock",
                    "message": message,
                },
            )
        elif "token" in text_data_json:
            token = text_data_json["token"]
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "get_user_from_token",
                    "token": token,
                },
            )

    def get_current_time(self):
        return str(localtime(now()))

    # Receive message from clock room
    async def check_clock(self, event):
        message = event["message"]
        print(message)

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    # "message": "fellow"
                    "cur_time": self.get_current_time()
                }
            )
        )

    async def get_exam(self, event):
        message = event["status"]

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {"status": message, "cur_time": self.get_current_time()}
            )
        )

    async def get_session_status(self, event):
        message = event["is_published"]

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {"session_status": message, "cur_time": self.get_current_time()}
            )
        )

    async def get_user_from_token(self, event):
        token = event["token"]
        auth = JWTAuthentication()
        try:
            valid_data = auth.get_validated_token(token)
            # Send user id to WebSocket
            response = {
                "user_id": valid_data["user_id"],
                "cur_time": self.get_current_time(),
            }

        except Exception as e:
            print(e)
            response = {"user": "", "error": "Invalid Token"}

        await self.send(text_data=json.dumps(response))
