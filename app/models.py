from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class NeighbourHood(models.Model):
    name = models.CharField(max_length=20)
    location = models.ForeignKey(on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0)
    image = CloudinaryField('image',blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def create_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()
