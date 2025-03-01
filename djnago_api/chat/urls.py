from django.urls import path
from .views import RoomListCreateView, RoomDetailView, MessageListCreateView, MessageDetailView

urlpatterns = [
    # Room URLs
    path('rooms/', RoomListCreateView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),

    # Message URLs
    path('messages/', MessageListCreateView.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
]
