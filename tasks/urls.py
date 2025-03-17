from django.urls import path

from tasks.views import TodoListListView, TodoItemListView, TodoListCreateView, TodoItemCreateView, TodoItemUpdateView, \
    TodoListDeleteView, TodoItemDeleteView

urlpatterns = [
    path("", TodoListListView.as_view(), name="index"),
    path("list/<int:list_id>/", TodoItemListView.as_view(), name="list"),
    path("list/add/", TodoListCreateView.as_view(), name="list-add"),
    path("list/<int:pk>/delete/", TodoListDeleteView.as_view(), name="list-delete"),
    path("list/<int:list_id>/item/add/", TodoItemCreateView.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>", TodoItemUpdateView.as_view(), name="item-update"),
    path("list/<int:list_id>/item/<int:pk>/delete", TodoItemDeleteView.as_view(), name="item-delete"),
]