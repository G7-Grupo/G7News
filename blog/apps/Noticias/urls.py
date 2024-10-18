
from django.urls import path
from . import views
from .views import UpdatePostView, AddCategoriaView

app_name = 'apps.Noticias'

urlpatterns = [
#     blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("add_Categoria/",AddCategoriaView.as_view(), name="add_Categoria"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<int:pk>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),

]