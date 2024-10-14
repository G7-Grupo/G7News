from django.shortcuts import render


def Index(request):

    return render(request,'base.html')

def Contact(request):

    return render(request, 'contact.html')