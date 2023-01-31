import uuid

from django.db import models


# Create your models here.
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          db_index=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    description = models.TextField(null=True, blank=True, max_length=600)
    #demo_link = models.URLField(null=True, blank=True, max_length=2000)
    demo_link = models.CharField(null=True, blank=True, max_length=2000)
    source_link = models.CharField(null=True, blank=True, max_length=2000)
    source_link1 = models.URLField(null=True, blank=True, max_length=2000)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          db_index=True, primary_key=True, editable=False)
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner = models.ForeignKey
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=600, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          db_index=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
