from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

CATEGORY = (('', 'Category'), 
            ('s', 'Sneakers'),
            ('t', 'T-shirt'),
            ('p', 'Pants'))

class Product(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=1, choices=CATEGORY)
    image = models.ImageField(default='no_image.jpg', upload_to = 'product')
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} Product"

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk':self.pk})

    def save(self):
        
        super().save()
        new_image = Image.open(self.image.path)

        if new_image.height > 350 and new_image.width > 350:
            output_size = (350, 350)
            new_image.thumbnail(output_size)
            new_image.save(self.image.path)

