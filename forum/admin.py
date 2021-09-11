from django.contrib import admin

from .models import Post, Thread


class PostInline(admin.StackedInline):
    model = Post
    readonly_fields = ("pub_date",)
    extra = 0


class ThreadAdmin(admin.ModelAdmin):
    readonly_fields = ("pub_date",)
    inlines = [PostInline]


admin.site.register(Thread, ThreadAdmin)
# admin.site.register(Post)
