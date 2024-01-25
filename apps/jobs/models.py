from django.db import models

class Jobs(models.Model):
    images = models.ManyToManyField('Image', blank=True)
    price = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('active', 'Актуально'),
        ('inactive', 'Не актуально'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    start_datatime = models.DateTimeField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "Подработки"
        verbose_name_plural = "Подработки"

class Image(models.Model):
    image = models.ImageField(upload_to='job_images/')

    def __str_(self):
        return str(self.image)