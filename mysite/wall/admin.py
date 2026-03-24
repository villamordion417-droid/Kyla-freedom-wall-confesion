from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'candle_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content', 'user__username')
