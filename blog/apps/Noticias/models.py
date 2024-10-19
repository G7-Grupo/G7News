from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify

class Categoria(models.Model):
    name = models.CharField(max_length = 255)

    
    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('apps.Noticias:blogs')


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=130, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} - {self.title} ({self.dateTime})"
    
    def get_absolute_url(self):
        return reverse('apps.Noticias:blogs')


    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content

