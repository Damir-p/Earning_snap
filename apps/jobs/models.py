from django.db import models

class Jobs(models.Model):
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    price = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    data = models.DateTimeField(max_length=255)

    class Meta:
        verbose_name = "Подработки"
        verbose_name_plural = "Подработки"