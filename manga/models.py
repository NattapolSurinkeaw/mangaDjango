from django.db import models

# Create your models here.
class Category(models.Model):
    cate_name = models.CharField(max_length=100)
    display = models.BooleanField(default=True)
    priority = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cate_name

class Cartoon(models.Model):
    cate_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cartoons")
    name_cartoon = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True, null=True)
    priority = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_cartoon

class Episode(models.Model):
    cartoon_id = models.ForeignKey(Cartoon, on_delete=models.CASCADE, related_name="episodes")
    name_episode = models.CharField(max_length=255)

    def __str__(self):
        return self.name_episode


class ImageCartoon(models.Model):
    episode_id = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="episodes")
    title_image = models.CharField(max_length=255)
    image_link = models.ImageField(upload_to='images', blank=True, null=True)
    priority = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title_image
