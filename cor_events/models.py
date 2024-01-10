# models.py
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone

class EventModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/')
    thumbnail = models.ImageField(upload_to='event_thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.thumbnail:
            self.create_thumbnail()

    def create_thumbnail(self):
        if self.thumbnail:
            thumbnail_path = self.thumbnail.path

            # Open the existing thumbnail
            image = Image.open(thumbnail_path)
            (width, height) = image.size
            max_size = (300, 200)

            # Resize the thumbnail
            image.thumbnail(max_size, Image.ANTIALIAS)

            # Save the resized thumbnail
            thumb_name = f"thumb_{timezone.now().strftime('%Y%m%d%H%M%S')}.jpg"
            thumb_io = BytesIO()
            image.save(thumb_io, format='JPEG')

            # Save the resized thumbnail to the same field
            self.thumbnail.save(thumb_name, InMemoryUploadedFile(
                thumb_io, None, thumb_name, 'image/jpeg', thumb_io.tell, None
            ), save=False)

            thumb_io.close()
