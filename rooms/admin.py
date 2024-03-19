from django.contrib import admin

from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('_number','exam_collection_room','archive_room') 
    search_fields = ('number', )  
    list_filter = ( 'archive_room','exam_collection_room',)

    @admin.display(description="Número da sala")
    def _number(self, obj):
        return f"Sala {obj.number}"
    
admin.site.register(Room, RoomAdmin)