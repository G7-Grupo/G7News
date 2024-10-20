
from django.urls import path
from . import views
from .views import UpdatePostView, AddCategoriaView,UpdateCommentView, CategoriasView,some_view

app_name = 'apps.Noticias'

urlpatterns = [
#     blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<int:pk>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("add_Categoria/",AddCategoriaView.as_view(), name="add_Categoria"),
    path("delete_comment/<int:comment_id>/", views.Delete_comment, name="delete_comment"),
    path("edit_comment/<int:comment_id>/", UpdateCommentView.as_view(), name="edit_comment"),
    path("categorias/<str:cats>/", CategoriasView, name= "categorias"),
    path('categoria/<str:cats>/', some_view, name='categorias_detail'),
    
   
    path("search/", views.search, name="search"),

]