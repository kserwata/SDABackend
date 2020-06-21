from django.urls import path
from .views import register_view, login_view, logout_view, users, login_as


urlpatterns = [
    path('register', register_view, name="auth_register_view"),
    path('login', login_view, name="auth_login_view"),
    path('logout', logout_view, name="auth_logout_view"),
    path('users', users, name="auth_users_view"),
    path('users/<int:pk>/login_as', login_as, name="auth_users_login_as_view"),
]
