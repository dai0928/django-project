from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


app_name = "program"
urlpatterns = [
    path('main/', MainLesson.as_view(), name='main_menu'),
    path('main/lesson1/', Lesson1.as_view(), name='Lesson1'),
    path('main/Lesson2/', Lesson2.as_view(), name="Lesson2"),
    path('main/lesson3/', Lesson3.as_view(), name='Lesson3'),
    path('main/Lesson4/', Lesson4.as_view(), name="Lesson4"),
    path('main/Lesson5/', Lesson5.as_view(), name="Lesson5"),
    path('main/Lesson6/', Lesson6.as_view(), name="Lesson6"),
    path('main/Lesson7/', Lesson7.as_view(), name="Lesson7"),
    path('main/Lesson8/', Lesson8.as_view(), name="Lesson8"),
    path('main/Lesson9/', Lesson9.as_view(), name="Lesson9"),
    path('main/Lesson10/', Lesson10.as_view(), name="Lesson10"),
    path('main/Lesson11/', Lesson11.as_view(), name="Lesson11"),
    path('main/howto_css/', Css_Lesson.as_view(), name="Css_Lesson"),
    path('main/python/', Python.as_view(), name="Python"),
    path('main/howto_py', Python_Lesson.as_view(), name="Python_Lesson"),
    path('main/scraping/', Search_name.as_view(), name="Scraping"),
    path('main/Result/', search_list, name="result"),
]