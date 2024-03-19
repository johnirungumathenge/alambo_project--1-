from .models import Supervisor, Approved_records
from django import forms

class SupervisorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Supervisor
        fields = ['fullname','email','regno','img']

class SupervisorLogin(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# approved 
class ApprovedRecordsForm(forms.ModelForm):
    class Meta:
        model = Approved_records
        fields = ['work', 'week', 'week_day', 'date', 'time', 'approved', 'feedback', 'supervisor']
        labels = {
            'work': 'Work Description',
            'week': 'Week',
            'week_day': 'Week Day',
            'date': 'Date',
            'time': 'Time',
            'approved': 'Approval Status',
            'feedback': 'Feedback',
            'supervisor': 'Supervisor',
        }
        widgets = {
           'work': forms.Textarea(attrs={'rows': 3}),  # Specify the number of rows
           'date': forms.DateInput(attrs={'type': 'date'}),
           'time': forms.TimeInput(attrs={'type': 'time'}),
           'feedback': forms.Textarea(attrs={'rows': 3})
        }