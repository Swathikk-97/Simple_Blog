from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CustomUser,Blog
from django.core.paginator import Paginator
import os   


def home(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        place = request.POST["place"]
        about = request.POST["about"]

        if not (email and password and first_name and last_name and place and about):
            return HttpResponse("All fields are required", status=400)

        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse("User already exists", status=400)

        user = CustomUser.objects.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name,place = place,about = about
        )
        return redirect('login')

    return render(request, 'signup.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Fixed request data retrieval
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials", status=400)

    return render(request, 'login.html')


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = CustomUser.objects.get(email=request.user.email)  # Fetch user profile


    if request.method=='POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        place = request.POST["place"]
        about = request.POST["about"]

        CustomUser.objects.filter(email=request.user.email).update(
            email=email, password=password, first_name=first_name, last_name=last_name,place = place,about = about
        )
        return redirect('profile_view')

    return render(request, 'profile.html', {'profile': profile})

def create_blog(request):
    if request.method == 'POST':
        title= request.POST.get('title')
        content = request.POST.get('content')
        image= request.FILES.get('image')

        Blog.objects.create(author=request.user,title=title,content=content,image=image)
        return redirect("my_blogs")
    return render(request,'create_blog.html')

def my_blogs(request):
    blogs=Blog.objects.filter(author=request.user)
    return render(request,"my_blogs.html",{'blogs':blogs})


def all_blogs(request):
    blogs=Blog.objects.all()
    paginator=Paginator(blogs,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,"all_blogs.html",{'blogs':page_obj})




def edit_blog(request, id):
    blog = Blog.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        # Remove old image only if a new one is uploaded
        if image:
            if blog.image:  # Delete old image file
                old_image_path = blog.image.path
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

            blog.image = image  # Assign new image

        blog.title = title
        blog.content = content
        blog.save()  # Save using model's save method

        return redirect("my_blogs")

    return render(request, 'edit_blog.html', {'blog': blog})


def delete_blog(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return redirect("my_blogs")


def blog_detail(request,id):
    blog=Blog.objects.get(id=id)
  
    return render(request,'blog_detail.html',{'blog':blog})

def logout_user(request):
    logout(request)
    return redirect('login')
