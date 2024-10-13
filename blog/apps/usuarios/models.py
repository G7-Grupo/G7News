from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    slug=models.CharField(max_length=130)
    content=models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    # author= models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarios_blogposts')  # Cambiar el related_name
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='noticias_blogposts') # esto aria que no fuese obligatorio el campo
    #  
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')