from django.urls import path
from .views import register_view, login_view, logout_view, index_page


urlpatterns = [
    path('register', register_view, name="auth_register_view"),
    path('login', login_view, name="auth_login_view"),
    path('logout', logout_view, name="auth_logout_view")
]
