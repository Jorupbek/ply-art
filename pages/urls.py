from django.urls import path

from pages.views import home_page_view, contacts_page, about_us_page

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about-us/', about_us_page, name='about_us'),
    path('contacts/', contacts_page, name='contacts'),
]
