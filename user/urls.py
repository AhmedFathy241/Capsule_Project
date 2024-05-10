from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('logout', views.logout_view, name='logout'),
    path('index', views.index, name='index'),
    path('emptycart', views.emptycart, name='emptycart'),
    path('fullcart', views.fullcart, name='fullcart'),
    path('wish', views.wish, name='wish'),

]
