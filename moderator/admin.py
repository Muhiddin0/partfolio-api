from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.ModeratorTechnologyList)
admin.site.register(models.Moderator)
admin.site.register(models.Offer)
admin.site.register(models.Skil)
admin.site.register(models.ProjectImage)
admin.site.register(models.Project)