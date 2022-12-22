from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup_view, name='signup_view'),
    path('login', views.login_view.as_view(), name='login_view'),
    path('logout', views.logout.as_view(), name='logout'),
    path('friends', views.friends, name='friends'),
    path('friends/<int:pk>', views.friends, name='friends'),
    path('talk_room/<int:id>', views.talk_room, name='talk_room'),
    path('setting_username/<int:pk>', views.setting_username.as_view(), name='setting_username'),
    path('setting_status/<int:pk>', views.setting_status.as_view(), name='setting_status'),
    path('setting_profile/<int:pk>', views.setting_profile.as_view(), name='setting_profile'),
    path('setting_email/<int:pk>', views.setting_email.as_view(), name='setting_email'),
    path('setting_img/<int:pk>', views.setting_img.as_view(), name='setting_img'),
    path('setting_password', views.setting_password.as_view(), name='setting_password'),
    path('password_change_done', views.password_change_done.as_view(), name='password_change_done'),
    path('setting/<int:pk>', views.setting.as_view(), name='setting'),
    path('setting/12', views.setting.as_view(), name='setting'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('go_search', views.go_search, name='go_search'),
    path('search/<int:id>', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)