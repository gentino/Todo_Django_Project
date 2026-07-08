from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('create',views.create,name='create'),
    path('task_edit/<int:pk>/edit',views.task_edit,name='task_edit'),
    path('delete_task/<int:pk>/delete',views.delete_task,name='delete_task'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',LogoutView.as_view(), name="logout")

]
