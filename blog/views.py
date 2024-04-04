from django.shortcuts import render
from .models import Post


def post_list(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'blog/blog.html', context)


def post_view(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'blog/post.html', context)