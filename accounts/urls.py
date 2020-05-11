from django.urls import path
from . import views
urlpatterns = [
    path('accounts/',views.accounts_handler,name='accounts'),
    path('login/',views.login_handler,name="login"),
    path('signup/',views.signup_handler,name="signup"),
    path('logout/',views.logout_handler,name="logout")
]
