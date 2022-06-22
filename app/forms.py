from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["contacts", "image", "bio", "hood"]

class PostBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ["name", "address", "image", "details", "hood"]


class PostAnnouncement(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ["title", "details"]


class AddAmenity(forms.ModelForm):
    class Meta:
        model = Amenities
        fields = ["name", "location", "contact", "image"]