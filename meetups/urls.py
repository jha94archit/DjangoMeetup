from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all-meetup'),  # domain.com/meetups
    path('<slug:meetup_slug>/registration_successfull',
         views.confirm_registration, name='confirm-registration'),
    # domain.com/meetups/<dynamic-path-segment
    path('<slug:meetup_slug>',
         views.meetup_details, name='meetup-detail'),

]
