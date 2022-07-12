from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Product(models.Model):
    label = models.CharField(max_length=255)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    like=models.ManyToManyField(User, related_name='likes', blank=True)
    dislike=models.ManyToManyField(User, related_name='dislikes', blank=True)
    love=models.ManyToManyField(User, related_name='loves', blank=True)

    def __str__(self):
        return self.label