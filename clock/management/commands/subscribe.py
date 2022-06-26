import json

import redis
from django.core.management.base import BaseCommand
from rest_framework_simplejwt.authentication import JWTAuthentication

# from django.contrib.auth import get_user_model

auth = JWTAuthentication()
# User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = redis.StrictRedis(host="localhost", port=6379, db=1)
        # r = redis.StrictRedis(host="localhost", port=6379, db=1)

        p = r.pubsub()
        p.subscribe("nodeLdjango-node")
        for message in p.listen():
            # print(message)
            if message:
                m_type = message.get("type", "")
                m_pattern = message.get("pattern", "")
                m_channel = message.get("channel", "")
                data = message.get("data", "")
                # print(data)
                self.stdout.write(
                    self.style.SUCCESS(f"{m_type} {m_pattern} {m_channel} {data}")
                )
                try:
                    valid_data = auth.get_validated_token(data)
                    # print(valid_data)
                    # Send user id to WebSocket
                    # user = User.objects.get(id=valid_data.get('user_id'))
                    response = {"user_id": valid_data["user_id"]}
                    # response = {"user_id": user.__str__()}
                except Exception as e:
                    print(e)
                    response = {"user": "", "error": "Invalid Token"}
                    # Published data of that user => `data`
                self.stdout.write(f"{response}")
                r.publish("nodeLdjango-django", json.dumps(response))
