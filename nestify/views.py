from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        pass1 = request.POST.get('pass1', '')
        
        userName = User.objects.filter(username=username)
        userEmail = User.objects.filter(email=email)

        if userName.exists():
            messages.error(request, 'Username is already taken!')
            return redirect('signup')
        if userEmail.exists():
            messages.error(request, 'Email already exists!')
            return redirect('signup')
        customer = User.objects.create_user(username=username, email=email, password=pass1)
        customer.first_name = firstname
        customer.last_name = lastname
        customer.save()
        messages.info(request, 'Account Successfully Created!')
        return redirect('login')
    return render(request, "signup.html")

@csrf_exempt
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        user = authenticate(request, username=username, password=password)

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Username does not exists!')
            return redirect('login')

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Password!')
            return redirect('login')
    return render(request, 'login.html')

def handleLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'home.html', {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_detail.html', {"post": post})

@login_required(login_url='/login/')
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, f'{blog_post.title.capitalize()} blog is created successfully!')
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {"form": form})

@login_required(login_url='/login/')
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'{post.title.capitalize()} blog is updated successfully!')
            return redirect('post_detail', pk=pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_post.html', {"form": form})

@login_required(login_url='/login/')
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.error(request, f'{post.title.capitalize()} blog is deleted successfully!')
        return redirect('home')
    return render(request, 'delete_post.html', {"post": post})
    
