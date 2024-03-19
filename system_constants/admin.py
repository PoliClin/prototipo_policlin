from django.contrib import admin

from .models import Schedule, Weekdays


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('time',) 
    search_fields = ('time',)  

#admin.site.register(Schedule, ScheduleAdmin)


class WeekdaysAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',)  

#admin.site.register(Weekdays, WeekdaysAdmin)