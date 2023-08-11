from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as user_login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import UploadImage
from django.core.paginator import Paginator
# Create your views here.


# @login_required(login_url="user_login")
def home(request):
    if request.user.is_authenticated:
        images = UploadImage.objects.all()
        paginator = Paginator(images, 9)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "home.html", {"image": page_obj, "category": UploadImage.objects.all().values("category").distinct()})
    else:
        messages.warning(request, "Please Login In first!!")
        return redirect("user_login")


def display_categories(request, category):
    filter_images = UploadImage.objects.all().filter(category=category)
    paginator = Paginator(filter_images, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"image": page_obj, "category": UploadImage.objects.all().values("category").distinct()})


def register(request):
    if request.method == "POST":
        user = RegisterUser(request.POST)
        username = request.POST['username']
        if user.is_valid():
            user.save()

            messages.success(
                request, f"{username.capitalize()} Signed in Successfully")
            return redirect("user_login")
        else:
            messages.warning(request, "Registration Unsuccesfull !! Try Again")
            return redirect("register")

    fm = RegisterUser()
    return render(request, "register.html", {'form': fm})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            messages.success(
                request, f"{username.capitalize()} has Succesfully Logged In.")
            return redirect("home")
        else:
            messages.warning(request, f"Username Or Password is Incorrect")
            return redirect("user_login")
    loginform = LoginUser()
    context = {"form": loginform}
    return render(request, "login.html", context)


def user_logout(request):
    if request.user.is_authenticated:
        messages.success(
            request, f"{request.user.username} Logged off Succesfully!")
        logout(request)

    return redirect("user_login")


@login_required(login_url="user_login")
def upload_image(request):
    if request.method == "POST":
        user = request.user
        name = request.POST['image_name']
        img = request.FILES["image"]
        category = request.POST["category"]
        image = UploadImage(user=user, image_name=name,
                            image=img, category=category)
        image.save()
        messages.success(request, "Image Uploaded Successfully !")
        return redirect("home")
    form = UploadImageForm()

    return render(request, "upload_image.html", {"form": form})


def profile(request):
    user_images = UploadImage.objects.all().filter(user=request.user.id)
    try:
        user_info = UserInformation.objects.get(user=request.user.id)
    except:
        user_info = None
    return render(request, "profile.html", {"user_info": user_info, "user_images": user_images})


def view_image(request, id):
    image = UploadImage.objects.get(id=id)
    return render(request, "view_image.html", {"image": image})


def select_user(request, id):
    images = UploadImage.objects.all().filter(user=id)
    count = images.count()
    user_info = User.objects.get(id=id)
    return render(request, "selected_users_images.html", {"images": images, "user_info": user_info, "count": count})


def trail(request):
    return render(request, "try.html", {"image": UploadImage.objects.all()})
