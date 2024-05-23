"""
Asset_manager_I_think URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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
from django.urls import include, re_path, path
import Asset_manager_web_app.views

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    re_path(r'^$', Asset_manager_web_app.views.index, name='index'),
    re_path(r'^home$', Asset_manager_web_app.views.index, name='home'),
    path('upload', Asset_manager_web_app.views.import_csv, name='upload'),
    
    
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)