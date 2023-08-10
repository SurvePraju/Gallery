

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UploadImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}"


class UserInformation(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    contact = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to="profile_pictures/")

    def __str__(self) -> str:
        return f"{self.user}"
