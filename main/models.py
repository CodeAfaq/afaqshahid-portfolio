from django.db import models

# Create your models here.

class Project(models.Model):
        featured_image = models.ImageField(null=True, blank=True, upload_to='projects/')
        title = models.CharField(max_length=50, blank=False)
        description = models.TextField(max_length=200, blank=False)
        demo_link = models.CharField(max_length=2000, null=True, blank=True)
        source_link = models.CharField(max_length=2000, null=True, blank=True)

        def __str__(self):
            return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length= 1000, blank=False)

    def __str__(self):
        return self.name
