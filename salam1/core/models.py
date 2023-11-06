from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import re
from django_model_history_tracker.mixins import HistoryTrackerMixin

def profile_media_path(instance, filename):
    name = re.sub(" +", " ", str(instance.user.username))
    return "media/images/{0}/{1}/{2}".format("profiles", name.replace(" ", "_"), filename)

def post_media_path(instance, filename):
    name = re.sub(" +", " ", str(instance.title))
    return "media/images/{0}/{1}/{2}".format("posts", name.replace(" ", "_"), filename)


class Profile(HistoryTrackerMixin,models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE,related_name="profile_user")
    image = models.ImageField(_("user image"), upload_to=profile_media_path,null=True,blank=True)
    phone = models.CharField(_("phone"), max_length=20,null=True,blank=True)
    address = models.CharField(_("address"), max_length=50,null=True,blank=True)

    def __str__(self):
        return self.user.username

class Post(HistoryTrackerMixin,models.Model):
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE,related_name="post_author")
    title = models.CharField(_("title"), max_length=50)
    desc = models.TextField(_("description"),null=True,blank=True)
    image = models.ImageField(_("post image"), upload_to=post_media_path,null=True,blank=True)

    def __str__(self):
        return self.title
    
class Comment(HistoryTrackerMixin,models.Model):
    post = models.ForeignKey(Post, verbose_name=_("post"), on_delete=models.CASCADE,related_name="comment_post")
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE,related_name="comment_author")
    desc = models.TextField(_("description"),null=True,blank=True)
    is_hidden = models.BooleanField(_("is hidden"),default=False)
    class Meta:
        permissions = {
            ("can_hide_comment","can hide comment"),
        }

    def __str__(self):
        return self.post.title + " | " + self.author.username

class Image(models.Model):
    post = models.ForeignKey(Post, verbose_name=_("Images"), on_delete=models.CASCADE,related_name='post_images')
    image = models.ImageField(_("image"), upload_to=post_media_path,null=True,blank=True)

    def __str__(self):
        return self.post.title + str(self.id)