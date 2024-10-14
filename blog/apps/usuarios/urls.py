from django.urls import path
from . import views

app_name = 'apps.usuarios'

urlpatterns = [  
#     profile
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
    
#    user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
]