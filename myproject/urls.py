"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from myapp.views import *
from rest_framework.authtoken import views
from myapp.routers import router
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stu_list/',stu_list),
    # path('stu_detail/<int:pk>/',stu_detail),
    path('',include(router.urls)),
    # path('snippetlist/', SnippetList.as_view(), name='home'),
    # path('snippetdetail/<int:pk>/', SnippetDetail.as_view(), name='homee'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/',views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
# tokenobtainpair- generates token in pairs one for access token(5 minutes) for data access and other one for refresh token(24 hours)..
# with the help of refresh token we will genrate access token