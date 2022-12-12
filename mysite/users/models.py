from django.db import models
from django.utils import timezone

# Create your models here.
class Visit(models.Model):
    ip_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.ip_address:  # datetime.now()
            self.updated_at = timezone.now()
        return super(Visit, self).save(*args, **kwargs)