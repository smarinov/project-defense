from django.urls import path

from secondtech_app.views import homepage, about_page, view_devices, add_device, details_device, delete_device, \
    edit_device, view_smartphones, view_laptops, view_tablets

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about_page, name='about page'),
    path('devices/', view_devices, name='view devices'),
    path('smartphones/', view_smartphones, name='view smartphones'),
    path('tablets', view_tablets, name='view tablets'),
    path('laptops/', view_laptops, name='view laptops'),

    path('create/', add_device, name='add device'),
    path('details/<int:pk>', details_device, name='details device'),
    path('delete/<int:pk>', delete_device, name='delete device'),
    path('edit/<int:pk>', edit_device, name='edit device'),

]
