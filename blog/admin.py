from django.contrib import admin
from .models import Post, Comment
from .forms import PostForm, CommentForm

#class PostAdmin(admin.ModelAdmin):
#    form = PostForm
#admin.site.register(Post, PostAdmin)
admin.site.register(Post)
#class CommentAdmin(admin.ModelAdmin):
#    form = CommentForm
#admin.site.register(Comment, CommentAdmin)
admin.site.register(Comment)