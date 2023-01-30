from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post, Group

def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'template': template,
        'posts': posts,
    }
    return render(request, template, context)
    #return HttpResponse('Главная страница')


def group_posts(request, slug):
    template = 'posts/group_list.html'
    
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'template': template,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

