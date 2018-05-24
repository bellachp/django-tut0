
from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):

    # -sign in front of published_date indicates descending order
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blahhg/post_list.html', {'posts': posts})
