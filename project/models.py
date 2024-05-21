from django.db import models

from moderator.models import ModeratorTechnologyList

# Create your models here.
class ProjectImages(models.Model):
    image = models.FilePathField(path="/img")

    def __str__(self) -> str:
        return self.image.split('/')[-1]

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology_list = models.ManyToManyField(ModeratorTechnologyList)
    images = models.ManyToManyField(ProjectImages)
    reles_date = models.DateField(null=True, blank=True)
    link = models.URLField()

    def __str__(self) -> str:
        return self.title