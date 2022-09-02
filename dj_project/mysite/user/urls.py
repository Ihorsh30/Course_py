from django.urls import path
from .views import user, signup_view, signin_view, user_deactivate, logout_view, profile_edit, login_edit

urlpatterns = [
    path('user/', user, name='user'),
    path('user/edit', profile_edit, name='profile_edit'),
    path('user/log_edit', login_edit, name='login_edit'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('deactivate/', user_deactivate, name='user_deactivate'),
    path('logout/', logout_view, name='logout'),
]