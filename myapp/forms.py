from django import forms
   
# creating a form 
class DateTimeInput(forms.DateTimeInput):
    input_type='date'

class InputForm(forms.Form):
    start_time = forms.DateTimeField(label='Start Time :', input_formats='%Y-%m-%dT%H:%M:%SZ')
    end_time = forms.DateTimeField(label='End Time :',input_formats='%Y-%m-%dT%H:%M:%SZ')
    