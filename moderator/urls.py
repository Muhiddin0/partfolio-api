from django.urls import path
from . import views


urlpatterns = [
    path('', views.ModeratorListCreateView.as_view(), name='index'),
    path('<int:pk>', views.ModeratorRetrieveView.as_view(), name='index'),
    path('<int:pk>/projects', views.ModeratorProjectsListView.as_view(), name='index'),
]