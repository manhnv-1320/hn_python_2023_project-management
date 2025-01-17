from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup", views.SignUp.as_view(), name="signup"),
    path("verify/<str:uidb64>/<str:token>", views.Verify.as_view(), name="verify"),
    path("projects", views.create_project, name="create_project"),
    path("projects/<int:project_id>", views.update_project, name="update_project"),
    path(
        "projects/<int:project_id>/delete", views.delete_project, name="delete_project"
    ),
    path(
        "projects/<int:project_id>/stages", views.StageList.as_view(), name="stage_list"
    ),
    path(
        "projects/<int:project_id>/stages/<int:stage_id>",
        views.StageDetail.as_view(),
        name="stage_detail",
    ),
    path("projects/list", views.ProjectList.as_view(), name="project_list"),
]
