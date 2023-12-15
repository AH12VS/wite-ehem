from django.contrib import admin
from .models import PostModel, CommentModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    ordering = ("-publish", )
    list_display = ("__str__", "title", "slug", "author",
                    "created", "publish", "status")
    list_editable = ("status", )
    list_filter = ("author", "created", "publish", "status")
    search_fields = ("title", "slug", "author", "body")
    prepopulated_fields = {
        "slug": ("author", "title", "time_for_slg"),
        "tags": ("title", ), 
    }

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    ordering = ("-created", )
    list_display = ("__str__", )
    

