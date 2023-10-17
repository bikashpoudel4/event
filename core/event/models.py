from django.db import models

# Create your models here.
class EventModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/')
    thumbnail = models.ImageField(upload_to='event_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title