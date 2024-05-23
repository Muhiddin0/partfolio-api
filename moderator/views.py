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

class ModeratorProjectsRetriveView(generics.RetrieveAPIView):
    queryset = models.Moderator.objects.all()
    serializer_class = serializer.ProjectsSerializer

    def get(self, request, *args, **kwargs):
        self.queryset.filter(projects__id=kwargs['project_pk'])
        return super().get(request, *args, **kwargs)