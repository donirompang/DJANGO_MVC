from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html',{'blog':blog})


def input_blog(request):
    if(request.method == "POST"):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
            
    else:
        form = BlogForm()
    return render(request, 'blog/input_blog.html', {'form':form})
