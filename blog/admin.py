from django.contrib import admin
from .models import Post, Tag, Comment


admin.site.register(Tag)


admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'published_at')

admin.site.register(Post, PostAdmin)

