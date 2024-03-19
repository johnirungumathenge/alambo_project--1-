from .models import Student, UpdateDetails
from django import forms

class StudentForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ['Fullname','Email','Regno','Profile']

class StudentLogin(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# update details by student
class UpdateDetailsForm(forms.ModelForm):
    class Meta:
        model = UpdateDetails
        fields = ['work', 'week', 'week_day','Date', 'time', 'student']

        widgets = {
            'work': forms.Textarea(attrs={'rows': 5}),  # Specify the number of rows
           'Date': forms.DateInput(attrs={'type': 'date'}),
           'time': forms.TimeInput(attrs={'type': 'time'}),
        }