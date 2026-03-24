from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='freedom_posts',
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    candle_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.title:
            return f"{self.title} ({self.candle_count} candles)"
        return f"Post {self.id} ({self.candle_count} candles)"
