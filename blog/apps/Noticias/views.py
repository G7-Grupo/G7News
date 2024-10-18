from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from apps.usuarios.forms import ProfileForm, BlogPostForm
from django.views.generic import UpdateView
from django.contrib import messages


def blogs(request):
    print("Entrando a la vista blogs") 
    posts = BlogPost.objects.all().order_by('-dateTime')
    print(f"Posts: {posts}")  # Esto debería mostrar los posts en la consola
    return render(request, "Noticias/blog.html", {'posts': posts})

def blogs_comments(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog=post)
        comment.save()
    return render(request, "Noticias/blog_comments.html", {'post':post, 'comments':comments})

@login_required(login_url='/login')
def Delete_Blog_Post(request, pk):
    posts = BlogPost.objects.get(id=pk)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'Noticias/delete_blog_post.html', {'posts':posts})

def search(request):
    if request.method == "POST":
        searched = request.POST ['searched']
        posts = BlogPost.objects.filter(title__contains=searched)
        return render(request, "Noticias/search.html", {'searched':searched, 'posts':posts})
    else:
        return render(request, "Noticias/search.html", {})

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
            return render(request, "Noticias/blog.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "Noticias/add_blogs.html", {'form':form})
"""
@login_required(login_url='/login')
def add_blogs(request):
    if request.method == "POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.Categoria = Categoria.objects.get(id=request.POST.get('categoria_id'))
            blogpost.author = request.user
            blogpost.save()
            return redirect('apps.Noticias:blogs')  
    else:
        form = BlogPostForm()
    return render(request, "Noticias/add_blogs.html", {'form': form})

class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'Noticias/edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'Categoria', 'image']
    def form_valid(self, form):
        form.save()
        return redirect(reverse('apps.Noticias:blogs'))

class AddCategoriaView(CreateView):
    model = Categoria
    template_name = 'Noticias/add_Categoria.html'
    fields = '__all__'
  
   

