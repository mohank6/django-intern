from faker import Faker
from .models import Author, AuthorDetails, Genre, Post, Comment

fake = Faker()


def create_fake_author():
    return Author.objects.create(name=fake.name())


def create_fake_author_details(author):
    return AuthorDetails.objects.create(
        author=author,
        age=fake.random_int(min=18, max=80),
        address=fake.address(),
    )


def create_fake_genre():
    return Genre.objects.create(description=fake.word())


def create_fake_post(author, genre):
    return Post.objects.create(
        title=fake.sentence(),
        author=author,
        genre=genre,
        read_time=fake.random_int(min=1, max=30),
        tag=fake.word(),
    )


def create_fake_comment(post):
    return Comment.objects.create(post=post, content=fake.paragraph())


def generate_fake_data():
    authors = [create_fake_author() for _ in range(10)]
    genres = [create_fake_genre() for _ in range(3)]
    for author in authors:
        create_fake_author_details(author)
    for _ in range(20):
        author = fake.random_element(authors)
        genre = fake.random_element(genres)
        post = create_fake_post(author, genre)

        comments = []
        for _ in range(5):
            comments.append(create_fake_comment(post))
        post.comments.set(comments)
        post.save()
