from django.contrib import admin
from django.urls import path
from .views import GroupsListCreateView, GroupsDetail
from .views import CfpsListCreateView
from .views import EventsListCreateView


#for media
from django.conf import settings
from django.conf.urls.static import static


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Gospeak",
        default_version='v1',
        description="Gospeak",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="xyz@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', GroupsListCreateView.as_view(), name='group-list-create'),
    path('groups/<int:id>/', GroupsDetail.as_view(), name='group-detail'),

    path('cfps/', CfpsListCreateView.as_view(), name='cfps-list-create'),
    path('events/', EventsListCreateView.as_view(), name='cfps-list-create'),
    path('proposals/', EventsListCreateView.as_view(), name='proposals-list-create'),

    # Swagger JSON and YAML format
    path('swagger.<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Redoc UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
