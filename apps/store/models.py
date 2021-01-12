from django.db import models
from io import BytesIO
from django.core.files import File
from django.db import models


# Create your models here.


class Category(models.Model):
    Availability = (
        ('disponible', 'True'),
        ('non disponible', 'false')
    )
    categoryId = models.IntegerField(),
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=150)
    Keywords = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=14, choices=Availability)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    Availability = (
        ('disponible', 'True'),
        ('non disponible', 'false')
    )
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='media/uploads/')
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to='media/uploads/')
    price = models.FloatField()
    amount = models.IntegerField(null=True)
    details = models.TextField()
    status = models.CharField(max_length=14, choices=Availability)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True),

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
