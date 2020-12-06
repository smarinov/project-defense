from django.urls import path

from accounts.views import details_profile, register_user, login_user, logout_user, delete_profile, edit_profile, \
    change_password

urlpatterns = [

    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('register/', register_user, name='register user'),

    path('profile/<int:pk>/', details_profile, name='user profile'),
    path('delete/<int:pk>', delete_profile, name='delete profile'),
    path('edit/<int:pk>', edit_profile, name='edit profile'),
    path('change-password/<int:pk>', change_password, name='change password'),

]
