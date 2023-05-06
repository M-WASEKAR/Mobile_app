"""mobile_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from api import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_register, name='register'),
    path('login/', views.login_page, name='login'),
    path('user-list/', views.user_list, name='user_list'),
    path('user-list-filter/', views.user_list_filter, name='user_list_filter'),
    path('user-bulk-upload/', views.user_bulk_upload, name='user_bulk_upload'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/create/',  views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/',  views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/',  views.UserDeleteView.as_view(), name='user_delete'),

]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
