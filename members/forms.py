from django import forms
from events.models import Student
class ProfilePage(forms.ModelForm):
    class Meta: 
        model =Student 
        fields = ["student_image","student_tag","student_bio","student_linkedin"]
        widgets = {
            "student_tag" : forms.SelectMultiple(attrs = {
                "class":"form-control"
            }),
          
            "student_linkedin" : forms.URLInput(attrs = {
                "class" : "form-control"
            }),
            
        }