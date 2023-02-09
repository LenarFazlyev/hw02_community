from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Group, Post


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)

#def index(request):
#    posts = Post.objects.all()[:settings.LIMITS_IN_PAGE]
#    context = {
#        'posts': posts,
#    }
#    return render(request, 'posts/index.html', context)

@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'group': group
    }
    return render(request, 'posts/group_list.html', context)

#@login_required
#def group_posts(request, slug):
#    group = get_object_or_404(Group, slug=slug)
#    posts = group.posts.all()[:settings.LIMITS_IN_PAGE]
#    context = {
#        'group': group,
#        'posts': posts,
#    }
#    return render(request, 'posts/group_list.html', context)
