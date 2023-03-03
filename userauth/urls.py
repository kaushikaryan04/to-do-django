from django.urls import path
from .views import ListUsers , ShowToDo  ,getUserDetail ,getUserToDo

urlpatterns = [
    path('listuser' , ListUsers.as_view() ),
    path('todo/<int:id>' , ShowToDo.as_view() ),
    path('register/' ,  getUserDetail().as_view() , name = 'createUser'),
    path('detail/' , getUserDetail.as_view()),
    path('getodo/' , getUserToDo.as_view())
]

