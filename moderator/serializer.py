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
            'rezyume',
        ]
        depth = 2


class ProjectsSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        # Customize the response data here
        representation = super().to_representation(instance)
        
        for i in representation['projects']:
            i['views'] = ProjectViewCount.objects.filter(project__id=i['id']).count()
        
        return representation  
    
    class Meta:
        model = Moderator
        fields = [
            'projects',
        ]
        depth = 3
            
class ProjectsRetriveSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"
        depth = 2
    
    def get_views(self, obj):
        return ProjectViewCount.objects.filter(project=obj).count()

class ProjectViewsIncrementSerializer(serializers.Serializer):
    
    class Meta:
        model = ProjectViewCount
        fields = "__all__"

        
class TestSerializer(serializers.Serializer):
    
    class Meta:
        model = ProjectViewCount
        fields = "__all__"
        depth = 2