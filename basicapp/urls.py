from django.urls import path, re_path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="user_login"),
    path("upload-image/", views.upload_image, name="upload_image"),
    path("images/<str:category>/",
         views.display_categories, name="image_category"),
    path("logout/", views.user_logout, name="logout"),
    path("logged-in-user-profile/", views.profile, name="profile"),
    path("image/<int:id>", views.view_image, name="view_images"),
    path("try/", views.trail, name="try"),
    path("user-id-<int:id>/", views.select_user, name="selected_user_images"),
    path("update-user/<int:id>/", views.update_user, name="update_user"),
    path("delete-image/<int:id>/", views.delete_image, name="delete_image"),
]
