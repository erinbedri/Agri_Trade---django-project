from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from agri_trade.posts.forms import PostCommentForm
from agri_trade.posts import services as post_services
from agri_trade.posts.models import PostComment, Post


# def show_posts(request):
#     posts = post_services.get_all_posts()
#
#     context = {
#         'posts': posts,
#     }
#
#     return render(request, 'posts/show_posts.html', context)


class PostsListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/show_posts.html'


def show_post(request, pk):
    post = post_services.get_single_post(pk=pk)
    comments = post_services.get_all_comments(pk=pk)
    comments_count = comments.count()

    context = {
        'post': post,
        'comments': comments,
        'comments_count': comments_count,
    }

    return render(request, 'posts/show_post.html', context)


def show_comments(request, pk):
    post = post_services.get_single_post(pk=pk)
    comments = post_services.get_all_comments(pk=pk)
    comments_count = comments.count()

    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('posts:show comments', args=[str(pk)]))
    else:
        form = PostCommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comments_count': comments_count,
        'form': form,
        'is_liked': False
    }

    return render(request, 'posts/show_comments.html', context)


def like_comment(request, pk1, pk2):
    comment = get_object_or_404(PostComment, id=pk2)
    liked = False

    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
        liked = False
    else:
        comment.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('posts:show comments', args=[str(pk1)]))
