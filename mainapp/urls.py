from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('index/', views.Index.as_view(),name="index"),
    path('login/', views.Auth.as_view(),name="login"),
    path('logout/', views.logoutuser, name="logout"),
]
