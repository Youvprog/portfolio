from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    preview = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.title}'

