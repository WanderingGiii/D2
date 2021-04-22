from django.db import models
from datetime import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_ranking = models.FloatField(default = 0.0)

    def update_ranking(self):
        author_posts = Post.objects.filter(author = self.user_id)
        author_articles = author_posts.object.filter(cathegory = artile)
        for articles in author_articles:
            article_runking = sum([article.post_ranking * 3])
        author_comment_ranking = sum([r.comment_ranking for r in Comment.objects.filter(user = self.user)])
        all_comments_ranking = sum(r.comment_ranking for r in Comment.objects.filter(post__in = author_posts))
        self.user_ranking = article_runking + author_comment_ranking + all_comments_ranking
        self.save()
        return self.user_ranking

class Cathegory(models.Model):
    cathegory = models.CharField(max_length = 255, unique = True)

class Post(models.Model):
    ARTICLE = 'AR'
    NEWS = 'NW'

    POSTTYPE = [
        (ARTICLE, 'article'),
        (NEWS, 'news'),
    ]
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_type = models.CharField(
        max_length=2,
        choices=POSTTYPE,
        default=NEWS,
    )

    datetime = models.DateTimeField(auto_now_add = True)
    cathegory = models.ManyToManyField(Cathegory, through = 'PostCategory')
    title = models.CharField(max_length = 255)
    text = models.TextField(default = '')
    post_ranking = models.FloatField(default = 0.0)

    def like(self):
        self.post_ranking +=1
        self.save()

    def dislike(self):
        self.post_ranking -=1
        self.save()

    def preview(self):
        return str(self.text [:125], '...')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    cathegory = models.ForeignKey(Cathegory, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.TextField(default = '')
    comment_datetime = models.DateTimeField(auto_now_add = True)
    comment_ranking = models.FloatField (default = 0.0)

    def like(self):
        self.comment_ranking +=1
        self.save()

    def dislike(self):
        self.comment_ranking -=1
        self.save()
