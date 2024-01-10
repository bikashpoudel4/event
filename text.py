# #######################---MODEL---#######################
# models.py
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone

class EventModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/')
    thumbnail = models.ImageField(upload_to='event_thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and not self.thumbnail:
            self.create_thumbnail()

    def create_thumbnail(self):
        image = Image.open(self.image.path)
        (width, height) = image.size
        max_size = (300, 200)

        # Resize the image
        image.thumbnail(max_size, Image.ANTIALIAS)

        # Save the thumbnail
        thumb_name = f"thumb_{timezone.now().strftime('%Y%m%d%H%M%S')}.jpg"
        thumb_io = BytesIO()
        image.save(thumb_io, format='JPEG')

        self.thumbnail.save(thumb_name, InMemoryUploadedFile(
            thumb_io, None, thumb_name, 'image/jpeg', thumb_io.tell, None
        ), save=False)

        thumb_io.close()

# #######################---MODEL---#######################