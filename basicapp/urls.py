from django.urls import path, re_path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/",  login, name="user_login"),
    path("upload-image/",  upload_image, name="upload_image"),
    path("images/<str:category>/",
         display_categories, name="image_category"),
    path("logout/",  user_logout, name="logout"),
    path("logged-in-user-profile/",  profile, name="profile"),
    path("image/<int:id>",  view_image, name="view_images"),
    path("try/",  trail, name="try"),
    path("user-id-<int:id>/",  select_user, name="selected_user_images"),
    path("update-user-profile/<int:id>/",
         update_user, name="update_user"),
    path("delete-image/<int:id>/",  delete_image, name="delete_image"),
    path("edit-image/<int:id>/",  edit_image, name="edit_image"),

]
