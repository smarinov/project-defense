from django.urls import path

from secondtech_app.views import homepage, about_page, view_devices

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about_page, name='about page'),
    path('devices/', view_devices, name='view devices')
]
