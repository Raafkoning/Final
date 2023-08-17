from django.contrib import admin
from django.urls import path
from webersems import views
from users import views as user_views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('delete/', views.clear, name='clear'),
    path('semesters/', views.sems, name='sems'),
    path('classes/', views.classes, name='classes'),
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', user_views.profilepage, name='profile'),

]