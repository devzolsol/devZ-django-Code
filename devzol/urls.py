from django.contrib import admin
from django.urls import path
from base import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name='dashboard'),
    path("detail/<str:pk>", views.detail,),
    path("login", views.loginUser),
    path("logout", views.logoutUser),
    # update company
    path("update_company", views.updateCompany),
]
