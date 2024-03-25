from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class SearchLog(models.Model):
    query = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.query)
