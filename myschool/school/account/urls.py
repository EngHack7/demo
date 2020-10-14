from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login' , views.Login , name = 'login'),
    path('profile/<int:id>' , views.Profile , name = 'profile'),
    path('logout' , views.Logout , name = 'logout'),
    path('reg' , views.reg , name = 'reg'),
    path('g', views.GradesV , name ='grade'),
    path('subject/<int:id>' , views.SubjectV , name='subject'),
    path('exam/<int:id>' , views.FormsGoogle , name="exam"),
    path('videos/<int:id>' , views.VideosView , name="videos"),
    path('teacher/<int:id>' , views.Teacher , name = "teacherp"),
    path('toselect' , views.ToSelecStudent , name='search')
]