from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='panel_dashboard'),
    path("login/",views.login_view,name='panel_login'),
    path("logout/",views.logout_view,name='panel_logout'),
    path("admins/", views.admin_list, name="panel_admin_list"),
    path("admins/create/", views.admin_create, name="panel_admin_create"),
]
