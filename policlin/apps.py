from django.apps import AppConfig


class MyappconfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'policlin'

    def ready(self):
        from django.contrib import admin
        from django.contrib.auth.models import Group
        admin.site.unregister(Group)