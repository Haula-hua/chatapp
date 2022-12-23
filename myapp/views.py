from django.shortcuts import redirect, render, get_object_or_404
from .models import Room, SignUp
from django.contrib.auth.models import User
from .forms import SignUpForm, RoomForm, EmailChangeField, ImgChangeField, SearchForm, StatusChangeField, ProfileChangeField
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode
from django.db.models import Q
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas
from operator import itemgetter


#username重複について調べる！➧OK!!!
def index(request):
    return render(request, 'myapp/index.html')
        

class login_view(LoginView):
    template_name="myapp/login.html"
    redirect_field_name="myapp/friends.html/"
    next = "myapp/friends.html/"

def signup_view(request):
    if request.method=='POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = "sign up success"
            return render(request, 'myapp/index.html')
    else:
        form = SignUpForm()
        return render(request, 'myapp/signup.html', {'form': form})

@login_required
def friends(request):#問題search機能をつけるのであれば理想的だが、既に設定されている人としか話せない。
    friends = SignUp.objects.all()#searchをつくるときは、ここを変える！
    friends_list = []
    for friend in friends:
        friends_username = friends.annotate().values_list("username", flat=True)
        friends_list.append([friend, friends_username])
    room_list = []
    for friend, friends_username in friends_list:
        room = Room.objects.filter(Q(my_username=request.user, friend_username=friend)|Q(friend_username=request.user, my_username=friend)).order_by("datetime").last()
        if room:
            friend_name = friend.username
            friend_id = friend.id
            friend_img = friend.img
            datetime = room.datetime
            my_list = [room, friend_name, friend_img, friend.id, datetime]
            room_list.append(my_list)
        else:
            continue
    room_list = sorted(room_list, reverse=True, key=lambda x: x[4])
    context = {
        'room_list' : room_list,
        'friends_list': friends_list
    }
    return render(request, "myapp/friends.html", context)

@login_required
def talk_room(request, id): #iveのidが送られてくるfriend_usrnameにしていた。
    friend_username_id = User.objects.filter(id=id).last()#last()がないと、textsの結果が絞り込めなくなる。なぜ...。
    model = Room
    texts = Room.objects.filter(Q(my_username=request.user, friend_username=friend_username_id) | Q(friend_username=request.user, my_username=friend_username_id)).order_by("datetime")
    form = RoomForm()
    context = {
        "texts" : texts,
        "form": form,
        id: id,
        "friend_username_id": friend_username_id
        }
    if request.method=='POST':
        form = RoomForm(request.POST)
        if form.is_valid():#この時点でformがvaildのはずないのでは？➧null, blankをTrueにした。
            new_room=form.save(commit=False)
            new_room.my_username=request.user.signup
            new_room.friend_username=friend_username_id.signup
            new_room.save()
            return render(request, 'myapp/talk_room.html', context)
        else:
            return render(request, 'myapp/talk_room.html', context)#こちらにくる
    else:
        return render(request, 'myapp/talk_room.html', context)

class logout(LoginRequiredMixin, LogoutView):
    template_name="myapp/login.html"


class setting(LoginRequiredMixin, UpdateView):
    template_name = "myapp/setting.html"
    model = SignUp
    fields = ["private", ]
    def get_success_url(self):
        return reverse_lazy("myapp:setting")


class setting_username(LoginRequiredMixin, UpdateView):
    template_name = "myapp/setting_username.html"
    model = SignUp
    fields = ["username", ]
    def get_success_url(self):
        return reverse_lazy("myapp:setting")

class setting_profile(LoginRequiredMixin, UpdateView):
    template_name = "myapp/setting_profile.html"
    model = SignUp
    form_class= ProfileChangeField
    def get_success_url(self):
        return reverse_lazy("myapp:setting")

class setting_status(LoginRequiredMixin, UpdateView):
    template_name = "myapp/setting_status.html"
    model = SignUp
    form_class= StatusChangeField
    def get_success_url(self):
        return reverse_lazy("myapp:setting")


class setting_private(LoginRequiredMixin, UpdateView):
    template_name = "myapp/setting_private.html"
    model = SignUp
    fields = ["private", ]
    def get_success_url(self):
        return reverse_lazy("myapp:setting")

class setting_email(LoginRequiredMixin, UpdateView):
    template_name = "myapp/setting_email.html"
    model = SignUp
    form_class= EmailChangeField
    def get_success_url(self):
        context = {
            pk: pk
        }
        return reverse_lazy("myapp:setting", context)

class setting_password(LoginRequiredMixin, PasswordChangeView):
    success_url=reverse_lazy("myapp:password_change_done")
    template_name="myapp/setting_password.html"

class password_change_done(LoginRequiredMixin, PasswordChangeDoneView):
    template_name="myapp/password_change_done.html"



class setting_img(LoginRequiredMixin, UpdateView):
    template_name = "myapp/setting_img.html"
    model = SignUp
    form_class= ImgChangeField
    def get_success_url(self):
        return reverse_lazy("myapp:setting")

def go_search(request):#既にrequest.userとのRoomを持っているuserを外したい。
    form = RoomForm
    model = SignUp
    existing_rooms_list = list(Room.objects.filter(Q(my_username=request.user) | Q(friend_username=request.user)).values_list('my_username').distinct())
    existing_rooms_list2 = Room.objects.filter(Q(my_username=request.user) | Q(friend_username=request.user)).values_list('friend_username').distinct()
    public_user_list = []
    latest_public_user_list = []
    public = SignUp.objects.filter(private=False).all() #iveだけを外せる。iveのみはevaからの通信がある＝my_username=request.userになっている。
    for i in public:
        if not (i.id,) in existing_rooms_list and not (i.id,) in existing_rooms_list2:
            public_user_list.append(i)
    context={
        "latest_public_user_list": public_user_list,
        "form" : RoomForm,
        "existing_rooms_list": existing_rooms_list,
        "existing_rooms_list2": existing_rooms_list2
    }
    return render(request, "myapp/search.html", context)

@login_required
def search(request, id):
    if request.method=='POST': #searchに遷移している。直接viewsに飛びたい。
        model = SignUp
        my_name = SignUp.objects.get(username=request.user)
        friend_name = SignUp.objects.get(id=id)
        form = SearchForm(request.POST)
        if form.is_valid():
            new_room =form.save(commit=False)
            new_room.my_username = my_name
            new_room.friend_username = friend_name
            new_room.text = "Hello"
            new_room.save()
            return friends(request)
        return render(request, "myapp/search.html")

#================================================================================

@login_required
def profile(request, id):#username, icon, status-message, profile
    model=SignUp
    someone = User.objects.filter(id=id).last()
    context = {
        someone: someone,
        "someone": someone
    }
    return render(request, "myapp/profile.html", context)









    
