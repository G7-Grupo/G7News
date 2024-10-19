from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth  import authenticate,  login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, BlogPostForm
from django.views.generic import UpdateView
from django.contrib import messages




def user_profile(request, myid):
    post = BlogPost.objects.filter(id=myid)
    return render(request, "usuarios/user_profile.html", {'post':post})

def profile(request):
    return render(request, "usuarios/profile.html")

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method=="POST":
        form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "usuarios/profile.html", {'alert':alert})
    else:
        form=ProfileForm(instance=profile)
    return render(request, "usuarios/edit_profile.html", {'form':form})

def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        registrado_group = Group.objects.get(name='Registrado')
        user.groups.add(registrado_group)

        messages.success(request, "Registro exitoso. Por favor, inicia sesión.")

        return redirect('/usuarios/login') 

    return render(request, "usuarios/register.html")

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'usuarios/login.html')   
    return render(request, "usuarios/login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/usuarios/login')