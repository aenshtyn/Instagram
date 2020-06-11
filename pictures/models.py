from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    # password = models.PasswordField()
    picture = models.ImageField()
    bio = models.TextField()

    def __str__(self):
        return self.first_name

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length =30)
    caption = models.TextField()
    # profile = models.ForeignKey(Profile)
    # likes = models.
    # comments = models.
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image
    class Meta:
        ordering = ['pub_date']

    @classmethod
    def all_images(cls):
        images =  Image.objects.all()
        return images
