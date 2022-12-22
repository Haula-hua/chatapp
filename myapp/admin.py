from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp, Room
from django.template.defaultfilters import truncatechars, linebreaks

class SignUpAdmin(admin.ModelAdmin):
    form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)

admin.site.register(Room)