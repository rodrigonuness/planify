
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.UploadExcelView.as_view()),
    path('tasks/today/', views.TodayTasksView.as_view()),
    path('tasks/', views.AllTasksView.as_view()),
    path('tasks/<int:pk>/complete/', views.CompleteTaskView.as_view()),
]
