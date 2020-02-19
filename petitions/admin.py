from django.contrib import admin
from .models import Post, Vote, Comment, PostImage

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(PostImage)
