from django.urls import path

from secondtech_custom_admin.views import view_admin_landing_page, view_admin_all_devices, view_admin_all_users, \
    view_admin_current_user_devices

urlpatterns = [
    path('', view_admin_landing_page, name='admin landing page'),
    path('all-devices/', view_admin_all_devices, name='admin all devices'),
    path('all-users/', view_admin_all_users, name='admin all users'),
    path('all-devices-for-user/<int:pk>', view_admin_current_user_devices, name='admin all devices current user'),
]