from django.urls import path
from .views import chat_messages

urlpatterns = [
    path("chat/", chat_messages, name="chat-messages"),
]
