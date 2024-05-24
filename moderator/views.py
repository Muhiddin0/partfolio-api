from django.http import Http404
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
    serializer_class = serializer.ProjectsRetriveSerializer


    def get_object(self):
        moderator_pk = self.kwargs['pk']
        project_pk = self.kwargs['project_pk']
        
        # Ensure the project is associated with the given moderator
        try:
            moderator = models.Moderator.objects.get(pk=moderator_pk, projects__id=project_pk)
            project = moderator.projects.get(pk=project_pk)
        except models.Moderator.DoesNotExist:
            raise Http404("Moderator or Project not found")
        
        return project

    # def get(self, request, *args, **kwargs):
    #     self.queryset.get(projects__id=kwargs['project_pk']).projects
    #     return super().get(request, *args, **kwargs)