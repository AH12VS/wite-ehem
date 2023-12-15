from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from users.models import UserModel
from ckeditor_uploader.fields import RichTextUploadingField


class PublishedPostModel(models.Model):
    def get_queryset(self):
        return super(PublishedPostModel, self).get_queryset().filter(status="published")


class PostModel(models.Model):
    STATUS_FIELD = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=60)
    # body = models.TextField()
    body = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to="images/post-thumbnail/", blank=True, null=True)
    author = models.ForeignKey(
        UserModel, models.CASCADE, related_name="post_auth")
    slug = models.SlugField(unique="publish")
    status = models.CharField(
        max_length=10, choices=STATUS_FIELD, default="published")
    created = models.DateTimeField(default=timezone.now)
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published_manager = PublishedPostModel()
    tags = TaggableManager()

    time_for_slg = models.TimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish", )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:postdetail_page", kwargs={"pk": self.id, "slug": self.slug})
    
    def get_absolute_url_for_edit(self):
        return reverse("posts:postdetail_edit_page", kwargs={"pk": self.id, "slug": self.slug})
    


class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="comment_post")
    name = models.CharField(max_length=60)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

