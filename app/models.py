from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    read_time = models.PositiveIntegerField()
    comments = models.ManyToManyField('Comment', blank=True, related_name='comments')
    tag = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    author_details = models.OneToOneField(
        'AuthorDetails', on_delete=models.CASCADE, related_name='author_info', null=True
    )

    def __str__(self):
        return self.name


class AuthorDetails(models.Model):
    author = models.OneToOneField(
        'Author', on_delete=models.CASCADE, related_name='details'
    )
    age = models.PositiveIntegerField()
    address = models.TextField()
    genre = models.ManyToManyField('Genre', blank=True)


class Genre(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post')
    content = models.TextField()

    def __str__(self):
        return self.content
