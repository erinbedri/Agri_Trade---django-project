from django.shortcuts import render, get_object_or_404

from agri_trade.posts.models import Post


def show_posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/show_posts.html', context)


def show_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/show_post.html', context)
