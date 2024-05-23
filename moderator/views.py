from rest_framework import generics
from . import models
from . import serializer

# Create your views here.

class ModeratorListCreateView(generics.ListCreateAPIView):
    queryset = models.Moderator.objects.all()
    serializer_class = serializer.ModeratorSerializer

class ModeratorRetrieveView(generics.RetrieveAPIView):
    queryset = models.Moderator.objects.all()
    serializer_class = serializer.ModeratorSerializer

class ModeratorProjectsListView(generics.RetrieveAPIView):
    queryset = models.Moderator.objects.all()
    serializer_class = serializer.ProjectsSerializer