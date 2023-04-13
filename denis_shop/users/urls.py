from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

]