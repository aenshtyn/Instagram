from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=120)
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="I am", blank=True)


    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length =30, blank = True)
    caption = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    comments = models.ManyToManyField(User, related_name='comments', blank=True, )
    pub_date = models.DateTimeField(auto_now_add=True, null = True)


     
    @classmethod
    def all_pics(cls):
        pics = Image.objects.all()
        return pics


    class Meta:
        ordering = ['pub_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.name} Image'