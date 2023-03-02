from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


# Create your views here.
# this class will handle the get request to our endpoint
# createAPIView is a class that will handle the post request, whereas ListAPIView will handle the get request
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
