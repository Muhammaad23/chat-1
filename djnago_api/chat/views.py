from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import ChatMessage
from .serializers import ChatMessageSerializer

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def chat_messages(request):
    if request.method == "GET":
        queryset = ChatMessage.objects.all().order_by("-timestamp")
        serializer = ChatMessageSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
