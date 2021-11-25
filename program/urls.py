from django.urls import path
from .views import Index, CreateAccount, AccountLogin, MainLesson
from django.contrib.auth import views as auth_views


app_name = "program"
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', CreateAccount.as_view(), name='create_account'),
    path('login/', AccountLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/', MainLesson.as_view(), name='main_menu')
]