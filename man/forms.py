from django import forms
from .models import Booking, Events, Feedback
from .models import Contact

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event', 'name', 'contact', 'email', 'booking_date']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['event'].queryset = Events.objects.all()
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name'})
        self.fields['contact'].widget.attrs.update({'placeholder': 'Your Contact Information'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email Address'})
        self.fields['booking_date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
        

# Feedback form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback_text']

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email'})
        self.fields['feedback_text'].widget.attrs.update({'placeholder': 'Your Feedback'})
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email','contactnumber', 'subject', 'message']


