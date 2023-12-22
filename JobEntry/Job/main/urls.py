from django.urls import path
from .views import *
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views



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
    path('accounts/login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
    path('<int:jobcreate_id>/like', like, name='like'),
    path('user/<int:id>/',UserPage.as_view(),name='user'),
    path('userform/',UserFormView.as_view(),name='userform'),
    path('searchuser/',SearchUser.as_view(),name='searchuser'),
    path('username/',SearchWorker,name='searchworker'),
    path('save/<int:id>/',Saves,name='saves'),
    path('savepage/',SavePage.as_view(),name='savepage'),
    path('talentsearch/',SerachTalent,name='searchtalent'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

            ]


