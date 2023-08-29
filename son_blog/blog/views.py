from django.shortcuts import render
from blog.models import Post
from .form import postForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def createForm(request):
    data = {}
    form = postForm(request.POST or None)
    if form.is_valid():
        form.save()
        return home(request)
    data['form'] = form
    return render(request,'form.html', data)


def update(request, pk):
    data = {}
    up_post = Post.objects.get(pk=pk)
    form = postForm(request.POST or None, instance=up_post)
    if form.is_valid():
        form.save()
        return home(request)
    data['form'] = form
    data['obj_delete'] = up_post
    return render(request, 'form.html', data)

def delete(request, pk):
    up_post = Post.objects.get(pk=pk)
    up_post.delete()
    return home(request)