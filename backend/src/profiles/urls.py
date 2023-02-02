from django.urls import path

from src.profiles import views 


urlpatterns = [
    path("me/", views.GetProfileAPIView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/", views.UpdateProfileAPIView.as_view(), name="update_profile"
    ),
    path("agents/all/", views.AgentListAPIView.as_view(), name="all-agents"),
    path("top-agents/all/", views.TopAgentsListAPIView.as_view(), name="top-agents"),
]
