from django.db import models
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    title = models.CharField(max_length=500, default="")
    post_content = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images", default="")
    admin_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images", default="")
    rate = models.FloatField(default=1,
                             validators=[
                                 MaxValueValidator(10),
                                 MinValueValidator(1)
                             ])

    def __str__(self):
        return self.reply_content
