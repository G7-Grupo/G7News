from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from apps.usuarios.forms import ProfileForm, BlogPostForm
from django.views.generic import UpdateView
from django.contrib import messages


""" def blogs(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    return render(request, "blog.html", {'posts':posts}) """

def blogs(request):
    posts = BlogPost.objects.all().order_by('-dateTime')  # Simplificado para obtener todos los posts ordenados
    return render(request, "blog.html", {'posts': posts})
""" 
def blogs_comments(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method =="POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post':post, 'comments':comments})
 """
def blogs_comments(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content', '')
        comment = Comment(user=user, content=content, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post': post, 'comments': comments})


def Delete_Blog_Post(request, slug):
    posts = BlogPost.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'delete_blog_post.html', {'posts':posts})
# search 1
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = BlogPost.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})


# search 2
""" def search(request):
    searched = request.GET.get('q', '')  # Cambiado a GET para facilitar la búsqueda
    blogs = BlogPost.objects.filter(title__icontains=searched) if searched else BlogPost.objects.none()
    return render(request, "search.html", {'searched': searched, 'blogs': blogs})
 """
# search 3
""" def search(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda desde la URL
    if query:
        blogs = BlogPost.objects.filter(title__icontains=query)  # Filtrar blogs que contienen el término de búsqueda
        searched = True
    else:
        blogs = BlogPost.objects.none()  # Si no hay búsqueda, no se mostrarán resultados
        searched = False

    context = {
        'blogs': blogs,
        'searched': searched,
    }
    return render(request, "search.html", context)
 """
    
@login_required(login_url = '/login')
def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "add_blogs.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "add_blogs.html", {'form':form})


class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'image']


