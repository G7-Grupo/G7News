from django.contrib import admin
from .models import *

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','content','dateTime',)
    search_fields = ('title','dateTime',)

admin.site.register(BlogPost, BlogPostAdmin)


admin.site.register(Comment)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','image','bio','phone_no','facebook', 'instagram', 'linkedin')
    search_fields = ('user','instagram','phone_no','facebook', 'linkedin')

admin.site.register(Profile, ProfileAdmin)
