from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('event/<str:pk>/', views.event_page, name='event'),
    path('event-register/<str:pk>/',views.event_register,name='event_register'),
    path('user/<str:pk>/',views.user_profile,name='user_profile'),
    path('account/',views.account_page,name='account'),
    path('project-submission/<str:pk>/',views.project_submission,name='project_submit'),
    path('update-submission/<str:pk>',views.update_submission,name='update_submission'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('logout/',views.logout_user,name='logout'),


]
