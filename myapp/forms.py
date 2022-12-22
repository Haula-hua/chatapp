from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import SignUp, Room
from django.utils.translation import gettext_lazy as _



class SignUpForm(UserCreationForm):
    class Meta:
        model = SignUp
        fields = ('username', 'email', 'password1', 'password2', 'img', 'private',"id")

class LoginForm(AuthenticationForm):
    def login_allowed(self, user):
        if not user.is_active:
            raise ValidationError()

class RoomForm(forms.ModelForm):
    text = forms.CharField(max_length=2000, required=True, help_text="enter message", widget=forms.Textarea())
    class Meta:
        model = Room
        fields = ("my_username", "friend_username", "text", "datetime",)

class SearchForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ("my_username", "friend_username")

class EmailChangeField(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = SignUp
        fields=("email", )

class ImgChangeField(forms.ModelForm):
    class Meta:
        model = SignUp
        fields=("img", )

class StatusChangeField(forms.ModelForm):
    status_message=forms.CharField(required=True, widget=forms.Textarea())
    class Meta:
        model = SignUp
        fields=("status_message", )

class ProfileChangeField(forms.ModelForm):
    profile=forms.CharField(required=True, widget=forms.Textarea())
    class Meta:
        model = SignUp
        fields=("profile", )

    

        