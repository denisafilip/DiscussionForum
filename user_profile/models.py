from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", default="default/user.png")
    birthday = models.DateField(blank=True, default="2000-07-02", help_text="Format: YYYY-MM-DD")
    age = models.IntegerField(blank=True, default="21", help_text="Your current age.")
    country = models.CharField(max_length=30, default="Romania", blank=True, help_text="Your country of origin.")
    city = models.CharField(max_length=30, default="Oradea", blank=True, help_text="Your city of origin.")


class Statistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    visit_count = models.IntegerField(blank=True, default=0)
    post_count = models.IntegerField(blank=True, default=0)
    reply_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"Statistics for user {self.user.username}:\n" \
               f"    Number of website visits: {self.visit_count};\n" \
               f"    Number of posts created: {self.post_count};\n" \
               f"    Number of replies posted: {self.reply_count}.\n"
