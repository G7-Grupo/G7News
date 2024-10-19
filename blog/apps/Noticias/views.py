from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
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
def Delete_comment(request, comment_id):
    
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
        
    if request.method == "POST":
        comment.delete()  
        return redirect(reverse('Noticias:blogs_comments', kwargs={'slug': comment.blog.slug}))
    return render(request, 'Noticias/delete_comment.html', {'comment': comment})

@login_required(login_url='/login')
def Delete_Blog_Post(request, pk):
    posts = BlogPost.objects.get(id=pk)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'Noticias/delete_blog_post.html', {'posts':posts})


class UpdateCommentView(UpdateView):
    model = Comment
    template_name = 'Noticias/edit_comment.html'
    fields = ['content']

    def get_object(self, queryset=None):
        comment_id = self.kwargs.get('comment_id')
        return get_object_or_404(Comment, id=comment_id)

    def form_valid(self, form):
        form.save()
        return redirect(reverse('apps.Noticias:blogs_comments', kwargs={'slug': self.object.blog.slug}))

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
            blogpost.author = request.user
            blogpost.save()
            return redirect('apps.Noticias:blogs')  
    else:
        form = BlogPostForm()
    return render(request, "Noticias/add_blogs.html", {'form': form})

class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'Noticias/edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'categoria', 'image']
    def form_valid(self, form):
        form.save()
        return redirect(reverse('apps.Noticias:blogs'))

class AddCategoriaView(CreateView):
    model = Categoria
    template_name = 'Noticias/add_Categoria.html'
    fields = '__all__'
  
def CategoriasView(request, cats):
    categoria_instance = get_object_or_404(Categoria, name=cats)
    categoria_posts = BlogPost.objects.filter(categoria=categoria_instance)
    return render(request, 'Noticias/categorias.html',{'cats':cats, 'categoria_posts':categoria_posts})
   

