from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from django.core.files import File
import os

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        image = self.request.data.get('image')
        if image:
            event = serializer.save()
            event.thumbnail = self.create_thumbnail(image)
            event.save()
        else:
            serializer.save()

    def create_thumbnail(self, image):
        # Resize the image to create a thumbnail
        from PIL import Image
        from io import BytesIO

        image = Image.open(image)
        image.thumbnail((100, 100))
        thumbnail_io = BytesIO()
        image.save(thumbnail_io, 'JPEG', quality=85)
        thumbnail = File(thumbnail_io, name=os.path.basename(image.name))
        return thumbnail