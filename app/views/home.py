from django.shortcuts import render
from ..models import Post, Comment

# from .. import fake_data


def home(request):
    # fake_data.generate_fake_data()
    posts = Post.objects.all()
    return render(request, 'app/home.html', {'posts': posts})
