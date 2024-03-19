
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from .settings import APP_VERSION

admin.site.site_header = f"PoliClin v{APP_VERSION}"
admin.site.index_title = "Início"
admin.site.site_title = "Administração"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('admin/')),

]
