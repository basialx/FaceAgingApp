from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(null=True)
    n=models.IntegerField()
    def __str__(self):
        return self.caption
