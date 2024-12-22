from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users (models.Model):
    name = models.CharField(max_length=200)
    Phone = models.IntegerField() 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class vyakula(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[
            ('pilau', 'pilau'),
            ('biriani', 'biriani'),
            ('wali nyama', 'wali nyama'),
            ('kisinia', 'kisinia'),
            ('chips kuku','chips kuku'),
        ],
    )
    description = models.TextField() 
    image = models.ImageField(upload_to='location_images/', blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class vinywaji(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glass_no = models.PositiveIntegerField(default=1)  # Rating between 1-5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
