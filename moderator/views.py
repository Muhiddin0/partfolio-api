from django.http import Http404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
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
    
class IncrementProjectViewCountView(APIView):

    def post(self, request, *args, **kwargs):
        moderator_pk = self.kwargs['pk']
        project_pk = self.kwargs['project_pk']
        
        try:
            # Ensure the project is associated with the given moderator
            moderator = models.Moderator.objects.get(pk=moderator_pk, projects__id=project_pk)
            project = moderator.projects.get(pk=project_pk)
        except models.Moderator.DoesNotExist:
            return Response({"error": "Moderator or Project not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Get the client's IP address
        ip_address = request.META.get('REMOTE_ADDR')
        
        # Check if this IP has already viewed this project
        viewer, created = models.ProjectViewCount.objects.get_or_create(ip=ip_address, project=project)
        
        if created:
            message = "View count incremented."
        else:
            message = "IP address already viewed this project."
        
        return Response({"message": message, "views": models.ProjectViewCount.objects.filter(project=project).count()}, status=status.HTTP_200_OK)
