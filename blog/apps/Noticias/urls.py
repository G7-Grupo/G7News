
from django.urls import path
# from . import views
from .views import search, blogs, blogs_comments, Delete_Blog_Post, add_blogs, UpdatePostView
# si se importan funciones y clases solo hay que poner el nombre como segundo parametro de path

app_name = 'Noticias'

urlpatterns = [
    path('', blogs, name='blogs'),
    path('blog/<str:slug>/', blogs_comments, name='blogs_comments'), # da igual usar str:slug o slug:slug
    path('add_blogs/', add_blogs, name='add_blogs'),
    path('edit_blog_post/<str:slug>/', UpdatePostView.as_view(), name='edit_blog_post'), # para identificar por ID los post 
    path('delete_blog_post/<slug:slug>/', Delete_Blog_Post, name='delete_blog_post'),
    path('search/', search, name='search'),
]
""" 
urlpatterns = [
    # blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),
]
urlpatterns = [
    path('', blogs, name='blogs'),
    path('blog/<slug:slug>/', blogs_comments, name='blogs_comments'), # da igual usar str:slug o slug:slug
    path('add_blogs/', add_blogs, name='add_blogs'),
    path('edit_blog_post/<int:pk>/', UpdatePostView.as_view(), name='edit_blog_post'), # para identificar por ID los post 
    path('delete_blog_post/<slug:slug>/', Delete_Blog_Post, name='delete_blog_post'),
    path('search/', search, name='search'),
    
] """