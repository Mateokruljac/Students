from django import forms 
from .models import Event, Venue 

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["event_title","event_venue","event_started","event_ended","event_capacitety","event_tag","event_description","event_date","event_website","event_email"]
        widgets = {
            "event_title":forms.TextInput(attrs = {
                "placeholder" : "title",
                "class":"form-control"
                }),
            "event_venue":forms.Select(attrs = {
                "class":"form-control"
                }),
            "event_started":forms.TimeInput(attrs = {
                "class":"form-control"
                }),
            "event_ended":forms.TimeInput(attrs = {
                "class":"form-control"
                }),
            "event_date":forms.DateInput(attrs = {
                "class":"form-control"
                }),
             "event_tag":forms.SelectMultiple(attrs = {
                 "class":"form-control"}),
            "event_description":forms.Textarea(attrs = {
                "class":"form-control"
                }),
           
            "event_booking":forms.SelectMultiple(attrs = {
                "class":"form-control"
                }),
            "event_website":forms.URLInput(attrs = {
                "class":"form-control"
                }),
            "event_email":forms.EmailInput(attrs = {
                "class":"form-control"
                }),
            "event_capacitety":forms.NumberInput(attrs = {
                "class":"form-control"
            })
        }
        
        labels = {
            "event_title" :"Title*:",
            "event_venue" :"Venue and address*:",
            "event_started" :"Start at (HH:MM:SS)*:",
            "event_ended" :"End at (HH:MM:SS)",
            "event_date" :"Date (YYYY:MM:DD)*:",
            "evennt_capacitety" :"Capacitety*:",
            "event_tag" :"Event tag (if you want to mark more event press ctrl + left click)*: ",
            "event_manager" :"Manager*:",
            "event_website" :"Webiste URL",
            "event_email" :"Email*",
        }

class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["event_title","event_venue","event_started","event_ended","event_tag","event_description","event_date","event_booking","event_website","event_email"]
        widgets = {
            "event_title":forms.TextInput(attrs = {
                "placeholder" : "title",
                "class":"form-control"
                }),
            "event_venue":forms.Select(attrs = {
                "class":"form-control"
                }),
            "event_started":forms.TimeInput(attrs = {
                "class":"form-control"
                }),
            "event_ended":forms.TimeInput(attrs = {
                "class":"form-control"
                }),
            "event_date":forms.DateInput(attrs = {
                "class":"form-control"
                }),
            "event_tag":forms.SelectMultiple(attrs = {
                "class":"form-control"
                }),
            "event_description":forms.Textarea(attrs = {
                "class":"form-control"
                }),
            "event_booking":forms.SelectMultiple(attrs = {
                "class":"form-control"
                }),
            "event_website":forms.URLInput(attrs = {
                "class":"form-control"
                }),
            "event_email":forms.EmailInput(attrs = {
                "class":"form-control"
                }),
        }
        
        labels = {
            "event_title" :"Title",
            "event_venue" :"Venue",
            "event_started" :"Start at (HH:MM:SS)",
            "event_ended" :"End at (HH:MM:SS)",
            "event_date" :"Date (YYYY:MM:DD)",
            "event_title" :"Title",
            "event_manager" :"Manager",
            "event_booking" :"Booking",
            "event_website" :"Webiste URL",
            "event_email" :"Email",
        }
        
class CreateVenueForm(forms.ModelForm):
    class Meta: 
        model = Venue
        fields = ["venue_name","venue_address"]
        widgets = {
            "venue_name":forms.TextInput(attrs = {
                "placeholder":"City",
                "class" : "form-control"
            }),
            "venue_address" : forms.TextInput(attrs={
                "placeholder" :"Address",
                "class" :"form-control"
            }),
            "venue_owner": forms.Select(attrs = { 
            "class"  : "form-control"
            })
        }

class UpdateVenueForm(forms.ModelForm):
    class Meta: 
        model = Venue
        fields = ["venue_name","venue_address"]
        widgets = {
            "venue_name":forms.TextInput(attrs = {
                "placeholder":"City",
                "class" : "form-control"
            }),
            "venue_address" : forms.TextInput(attrs={
                "placeholder" :"Address",
                "class" :"form-control"
            }),
            
        }