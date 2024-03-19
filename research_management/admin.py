from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group

from .forms import ResearchForm
from .models import Research, ScheduledTimes


class CustomAdminSite(AdminSite):
    def unregister_default(self):
        self.unregister(Group)

admin_site = CustomAdminSite(name='customadmin')
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'name', 'main_researcher', 'expected_number_of_patients','outpatient_care',) 
    search_fields = ('name', ',main_researcher', )  
    list_filter = ('main_researcher', ) 
    list_display_links = ('name',)

    form = ResearchForm
admin.site.register(Research, ResearchAdmin)

class ScheduleTimesAdmin(admin.ModelAdmin):

    list_display = ('research', '_main_researcher','room', '_start_schedule', '_end_schedule', '_weekdays')
    search_fields = ('start_schedule', 'end_schedule', 'room', 'research', 'weekday') 
    list_filter = ( 'room', 'research') 

    #form = ScheduledTimesForm

    @admin.display(description="Dias da semana")
    def _weekdays(self, obj):
        return ', '.join([weekday.name for weekday in obj.weekday.all()])
    
    @admin.display(description="Encarregado")
    def _main_researcher(self, obj):
        return obj.research.main_researcher

    @admin.display(description="Horário de início")
    def _start_schedule(self, obj):
        return obj.start_schedule.time.strftime("%H:%M") + "h"
    
    @admin.display(description="Horário de término")
    def _end_schedule(self, obj):
        return obj.end_schedule.time.strftime("%H:%M") + "h"

admin.site.register(ScheduledTimes, ScheduleTimesAdmin)