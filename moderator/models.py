from django.db import models

# Create your models here.
class Skil(models.Model):
    skil = models.CharField(max_length=100)
    skil_img = models.ImageField(upload_to="skils/")
    
    def __str__(self) -> str:
        return self.skil

class ModeratorTechnologyList(models.Model):
    skils = models.ForeignKey(Skil, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.skils.skil
        
class Offer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="offers/")
    link = models.URLField()
    
    def __str__(self) -> str:
        return self.name

        
# Create your models here.
class ProjectImage(models.Model):
    image = models.ImageField(upload_to="projects/")
    
    def __str__(self) -> str:
        return self.image.url.split('/')[-1]

class ProjectVideo(models.Model):
    video_url = models.URLField()
    
    def __str__(self) -> str:
        return self.video_url

        
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology_list = models.ManyToManyField(ModeratorTechnologyList)
    images = models.ManyToManyField(ProjectImage)
    videos = models.ManyToManyField(ProjectVideo, blank=True)
    reles_date = models.DateField(null=True, blank=True)
    link = models.URLField()

    def __str__(self) -> str:
        return self.title


class Moderator(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    expirence = models.IntegerField()
    position = models.CharField(max_length=100)
    description = models.TextField()
    profile = models.ImageField(upload_to="profile/")
    
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    tiktok = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    location = models.URLField(max_length=100, null=True, blank=True)

    skil_list = models.ManyToManyField(ModeratorTechnologyList, blank=True)
    offer = models.ManyToManyField(Offer, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    
    def __str__(self):
        return self.name

        
class ProjectViewCount(models.Model):
    ip = models.CharField(max_length=25, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.ip