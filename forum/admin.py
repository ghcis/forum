from django.contrib import admin

from .models import Post, Thread


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class ThreadAdmin(admin.ModelAdmin):
    inlines = [PostInline]


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post)
