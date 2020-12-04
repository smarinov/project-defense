from django.urls import path

from accounts.views import details_profile, register_user, login_user, logout_user, delete_profile

urlpatterns = [

    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('register/', register_user, name='register user'),

    path('profile<int:pk>/', details_profile, name='user profile'),
    path('delete/<int:pk>', delete_profile, name='delete profile')

]
