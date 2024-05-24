from django.urls import path
from . import views

urlpatterns = [
    path('', views.ModeratorListCreateView.as_view(), name='index'),
    path('<int:pk>', views.ModeratorRetrieveView.as_view(), name='moderator-detail'),
    path('<int:pk>/projects', views.ModeratorProjectsListView.as_view(), name='moderator-projects'),
    path('<int:pk>/projects/<int:project_pk>', views.ModeratorProjectsRetriveView.as_view(), name='moderator-project-details'),
    path('<int:pk>/projects/<int:project_pk>/increment', views.IncrementProjectViewCountView.as_view(), name='increment-project-view-count'),
]