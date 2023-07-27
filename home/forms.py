from django import forms

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {

            'pat_name':'Patient Name: ', 
            'pat_phone':'Patient Contact Number: ',
            'pat_email':'Patient Email Address: ',
            'doc_name': 'Doctor Name: ',
            'booking_date':'Appointment Date'
           
        }
        