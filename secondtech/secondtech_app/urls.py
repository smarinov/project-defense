from django.urls import path

from secondtech_app.views import homepage, about_page

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about_page, name='about page')
]
