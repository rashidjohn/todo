from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='task'),
    path("task-create/", TaskCreate.as_view(), name="task_create"),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task_edit"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task_delete"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", RegisterPage.as_view(), name="register")
]