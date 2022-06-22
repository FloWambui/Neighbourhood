from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class NeighbourHood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    occupants_count = models.IntegerField(default=0)
    image = CloudinaryField('image',blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def create_neighbourhood(self):
        self.save()

    def save_neighbourhood(self):
        return self.save()


    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()

class Amenities(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    contact = models.CharField(max_length=30)
    image = CloudinaryField('image',blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)

    def save_amenities(self):
        self.save()

    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image',blank=True)
    bio = models.CharField(max_length=255, blank=True)
    contacts = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Business(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image',blank=True)
    details = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ["-create_date"]



class Announcements(models.Model):
    title = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_on']