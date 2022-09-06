from django.urls import path
from .views import user, Signup, Login, user_deactivate, ProfileEdit, LoginEdit, Logout, DeleteUser, PasswordChange

urlpatterns = [
    path('user/', user, name='user'),
    path('user/edit/', ProfileEdit.as_view(), name='profile_edit'),
    path('user/log_edit/', LoginEdit.as_view(), name='login_edit'),
    path('password/', PasswordChange.as_view(), name='password_change'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('deactivate/', user_deactivate, name='user_deactivate'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user/delete/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
]
