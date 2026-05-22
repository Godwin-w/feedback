from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedbacks/', views.view_feedbacks, name='feedback_list'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]