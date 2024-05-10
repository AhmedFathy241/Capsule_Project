from django.urls import path
from . import views

urlpatterns = [
    path('haircare', views.haircare, name="haircare"),
    path('makeup', views.makeup, name="makeup"),
    path('babymom', views.babymom, name="babymom"),
    path('medication', views.medication, name="medication"),
    path('skincare', views.skincare, name="skincare")

]