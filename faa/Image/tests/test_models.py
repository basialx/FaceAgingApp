from django.test import TestCase
from Image.models import Image
from django.core.files.images import ImageFile
"""
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField()
    def __str__(self):
        return self.caption
"""

class ImageModelTestCase(TestCase):
    def setUp(self):
        self.image = Image(caption="k", image=ImageFile(open('C:/Users/patkr/faa/media/alan.jpg', 'rb')))

    def test_image_creation(self):
        self.image.save()
        self.assertIsNotNone(self.image.id)

