from rest_framework import serializers
from .models import *
from project.models import *

class ModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = [
            'id',
            'name',
            'birth_date',
            'expirence',
            'position',
            'description',
            'profile',
            'telegram',
            'instagram',
            'youtube',
            'tiktok',
            'linkedin',
            'twitter',
            'facebook',
            'location',
            'skil_list',
            'offer',
        ]
        depth = 2

class ProjectsSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField()

    class Meta:
        model = Moderator
        fields = [
            'projects',
        ]
        depth = 2
            
    def get_views(self, obj):
        return ProjectViewCount.objects.filter(project=obj).count()


class ProjectsRetriveSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"
        depth = 2
    
    def get_views(self, obj):
        return ProjectViewCount.objects.filter(project=obj).count()

class ProjectViesIncreaseSerializer(serializers.Serializer):
    
    class Meta:
        model = ProjectViewCount
        fields = "__all__"