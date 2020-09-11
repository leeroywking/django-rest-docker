from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Cars(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    make = models.CharField(max_length=24)
    model = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    name = models.TextField()
    country_of_origin = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name