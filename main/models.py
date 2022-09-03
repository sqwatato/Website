from pyexpat import model
from django.db import models
from django.utils.timezone import now


# Projects
class Project(models.Model):
    title = models.TextField(max_length=100)
    blurb = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(default=now(), blank=True, null=True)
    featured = models.BooleanField(default=False)
    image = models.TextField(max_length=30)
    website_link = models.URLField(default=None, blank=True, null=True)
    github = models.URLField(default=None, blank=True, null=True)
    

# Tags for Projects
class ProjectTag(models.Model):
    name = models.TextField(max_length=25)
    projects = models.ManyToManyField(Project, related_name="tags", blank=True, null=True)

# Contact Message Object
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()