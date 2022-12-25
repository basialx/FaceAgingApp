from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True, upload_to="image/%y") #
    def __str__(self):
        return self.caption

def upload_loaction(instance,filename):
    location = str(instance.name)
    return "Image/%s/%s" %(location,filename)