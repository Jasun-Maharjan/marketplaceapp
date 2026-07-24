from django.shortcuts import render, get_object_or_404
from .models import Blog

def blogs(request):
    blogs = Blog.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blogs/blogs.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, published=True)
    return render(request, 'blogs/details.html', {'blog': blog})
