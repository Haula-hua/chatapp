from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class SignUp(User):
    img = models.FileField(upload_to="img", default="img/buta1.jpg")
    private = models.BooleanField(default=False, help_text="check to create a private account")
    status_message =models.CharField(max_length=40, blank=True, null=True)
    profile = models.CharField(max_length=140, blank=True, null=True)
    fields = ("username", "email", "password1", "password2", "img", "private", "id", "status_message", "profile")

    def __str__(self):
        return self.username

class Room(models.Model):
    my_username = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name="my_username", blank=True, null=True)
    friend_username = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name="friend_username", blank=True, null=True)
    text = models.CharField(max_length=2000, blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return "{}'s Room with {}".format(self.my_username, self.friend_username)

