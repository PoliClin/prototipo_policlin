from django import forms
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Research, ScheduledTimes


class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['researchers'].queryset = User.objects.filter(username__icontains='pesquisador')
        self.fields['main_researcher'].queryset = User.objects.filter(username__icontains='pesquisador')

class ScheduledTimesForm(forms.ModelForm):
    class Meta:
        model = ScheduledTimes
        fields = ['start_schedule', 'end_schedule', 'weekday', 'research', 'room']

    def clean(self):
        cleaned_data = super().clean()
        start_schedule = cleaned_data.get('start_schedule')
        end_schedule = cleaned_data.get('end_schedule')
        weekday = cleaned_data.get('weekday')
        room = cleaned_data.get('room')

        if start_schedule and end_schedule and weekday and room:
            existing_object = ScheduledTimes.objects.filter(start_schedule=start_schedule, room=room, weekday=weekday)
            if existing_object.exists():
                raise forms.ValidationError("Já existe um objeto com o mesmo início, fim, dia da semana e sala.")
                
        return cleaned_data
