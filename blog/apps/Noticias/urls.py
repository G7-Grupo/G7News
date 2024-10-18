
from django.urls import path
from . import views
from .views import UpdatePostView, AddCategoriaView,UpdateCommentView

app_name = 'apps.Noticias'

urlpatterns = [
#     blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("add_Categoria/",AddCategoriaView.as_view(), name="add_Categoria"),
    path("delete_comment/<int:comment_id>/", views.Delete_comment, name="delete_comment"),
    path("edit_comment/<int:comment_id>/", UpdateCommentView.as_view(), name="edit_comment"),
    
   
    path("search/", views.search, name="search"),

]