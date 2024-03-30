from rest_framework.response import Response
from rest_framework.decorators import api_view
from baseapp import models
from . import serializers

@api_view(http_method_names=['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/rooms', 
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(http_method_names=['GET'])
def getRooms(request):
    rooms = models.Room.objects.all()
    serializer = serializers.RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def getRoom(request, pk):
    room = models.Room.get(id=pk)
    serializer = serializers.RoomSerializer(room, many=False)
    return Response(serializer.data)