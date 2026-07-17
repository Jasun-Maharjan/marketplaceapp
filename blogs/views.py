from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog_list(request):
    page = get_object_or_404(Blog)
    return render(request, 'extending/blogs.html',{'page':page})
