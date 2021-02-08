"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from django.conf.urls import url

schema_url_v1_patterns = [
    path('v1/', include('snippets.urls')),
]
 
schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Eunji Open API",
        default_version='v1',
        description="안녕하세요. Eunji Open API 문서 페이지 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="Jay@google.com"),
        license=openapi.License(name="Jay's CodeFactory"),
    ),
    validators=['flex'], #'ssv'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v1_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('snippets.urls')),

     # Auto DRF API docs
    url(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/v1/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/v1/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]
