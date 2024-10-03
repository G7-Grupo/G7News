from django.contrib import admin
from .models import *
from .models import Libro,Autor

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha_publicacion',)
    search_fields = ('isbn','titulo',)


admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor)

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Profile)