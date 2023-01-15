from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('', views.Index.as_view(),name="index"),
    path('login/', views.Auth.as_view(),name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('aboutus/', views.aboutus.as_view(), name="aboutus"),
    path('addsocial/', views.AddSocial.as_view(), name="addsocial"),
]
