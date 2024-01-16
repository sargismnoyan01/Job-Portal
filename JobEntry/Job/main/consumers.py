# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from .models import Likes

# class LikeConsumer(AsyncWebsocketConsumer):
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         user = text_data_json["user"]
#         jobcreate = text_data_json["jobcreate"]

#         await self.save_message(user,jobcreate)


#     @database_sync_to_async
#     def save_message(self, user, jobcreate):
#         Likes.objects.create(user=user, jobcreate=jobcreate)

