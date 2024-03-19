from django import forms

from .models import Schedule


# class ScheduledTimesForm(forms.ModelForm):
#     class Meta:
#         model = Schedule
#         fields = ['research', 'room', 'start_schedule', 'end_schedule', 'weekday']
#         widgets = {
#             'weekday': forms.SelectMultiple(attrs={'class': 'form-control'}),
#         }