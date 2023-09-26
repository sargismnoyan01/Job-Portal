from django.urls import path
from .views import *
from django.conf.urls import handler404


handler404 = 'main.views.custom_404_view'

urlpatterns=[
    path('',HomeListView.as_view(),name='home'),
    path('search/',SearchWord,name='search'),
    path('create/',CreateDetalView.as_view(),name='create'),
    path('joblist/',JobListView.as_view(),name='joblist'),
    path('<int:id>/',JobDetail.as_view(),name='detail'),
    path('about/',AboutDetalView.as_view(),name='about'),
    path('testimonial/',TestimonialView.as_view(),name='testimonial'),
    path('resiume/',Resiume.as_view(),name='resiume'),
    path('talent/',TalantListView.as_view(),name='talent'),
    path('talent/<int:id>/',TalentDetailView.as_view(),name='talentdetail'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('register/',Register,name='register'),
    path('login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
    path('<int:jobcreate_id>/like', like, name='like'),
    path('user/<int:id>/',UserPage.as_view(),name='user'),
    path('userform/',UserFormView.as_view(),name='userform'),
    path('searchuser/',SearchUser.as_view(),name='searchuser'),
    path('username/',SearchWorker,name='searchworker'),
    path('save/<int:id>/',Saves,name='saves'),
    path('savepage/',SavePage.as_view(),name='savepage')
    

            ]


