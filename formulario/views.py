from django.shortcuts import render
from .models import Post

def post_list(request):
    return render(request, 'formulario/post_list.html', {})
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
