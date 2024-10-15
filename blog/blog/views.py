from django.shortcuts import render, redirect


def Index(request):

    return redirect('apps.Noticias:blogs')

def Contact(request):

    return render(request, 'contact.html')