from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html',{'blog':blog})


def input_blog(request):
    if(request.method == "POST"):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
            
    else:
        form = BlogForm()
    return render(request, 'blog/input_blog.html', {'form':form})


def blog_detail(request, blog_id):
    blogging = Blog.objects.get(pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'b':blogging})
