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
    class Meta:
        model = Moderator
        fields = [
            'projects',
        ]
        depth = 2