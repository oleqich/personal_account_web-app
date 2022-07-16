from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='users'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
]
