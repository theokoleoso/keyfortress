from django.urls import path
from .views import CustomPasswordChangeView, CustomPasswordChangeDoneView, Profile, Tips, About

urlpatterns = [
    path('password/change', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password/change/done', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile', Profile.as_view(), name='profile'),
    path('tips', Tips.as_view(), name='tips'),
    path('about', About.as_view(), name='about'),
]
