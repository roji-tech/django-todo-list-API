from django.urls import path
from .views import (
    delete_all_todos,
    list_todos,
    completedTodo,
    delete_all_todos,
    add_todos, del_todo,
    delete_completed
)


urlpatterns = [
    path("", list_todos, name="list"),
    path("add", add_todos, name="add"),
    path("delete/<int:pk>", del_todo, name="delete"),
    path("complete/<int:pk>", completedTodo, name="completed"),
    path("delete-completed", delete_completed, name="deletecompleted"),
    path("delete-all", delete_all_todos, name="deleteall"),
]
