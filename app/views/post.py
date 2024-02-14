from django.shortcuts import render
from ..models import Post, Comment
from django.shortcuts import get_object_or_404

def post(request, id):
    # fake_data.generate_fake_data()
    post = get_object_or_404(Post, id=id)   
    comments = Comment.objects.filter(post=post)
    return render(request, 'app/post.html', {'post': post, 'comments': comments})
    