import datetime
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Tag(models.Model):
    name = models.CharField("Tag name",max_length = 100)
    
    def __str__(self):
        return self.name

class Venue(models.Model):
    venue_name = models.CharField("Venue",max_length = 120,blank = False)
    venue_address = models.CharField(max_length = 120,blank = False)
    venue_owner = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.venue_address}, {self.venue_name}"

class Event(models.Model):
    event_title = models.CharField("Title",max_length = 100,blank = False,null = False)
    event_venue = models.ForeignKey(Venue,on_delete = models.CASCADE)
    event_started = models.TimeField("Start",blank = False,null = False)
    event_tag = models.ManyToManyField(Tag,related_name = "tags_for_event",blank = True,null = True)
    event_ended = models.TimeField("End",blank = True,null = True)
    event_date = models.DateTimeField("Date",blank = False)
    event_capacitety = models.IntegerField(blank = False)
    event_description =RichTextField()
    event_manager = models.ForeignKey(User,on_delete = models.CASCADE)
    event_booking = models.ManyToManyField(User,related_name = "booking_event", blank = True)
    event_website = models.URLField("URL",max_length = 100,blank = True,null = True)
    event_email = models.EmailField("Email",blank = False)
    
    def __str__(self):
        return self.event_title
    
    @property 
    def total_capacitety (self):
        return self.event_capacitety - self.event_booking.count()
    
    @property
    def days_till(self):
        time = datetime.date.today()
        print("Day:",time)
        day_till = self.event_date.date() - time
        if day_till.days == 0:
            return "Today"
        elif day_till.days < 0:
            return "Past"
        else:
            return day_till.days


class Student(models.Model):
    student_user = models.OneToOneField(User,on_delete = models.CASCADE,null = True)
    student_image = models.ImageField("Image",blank = True,upload_to = "images/")
    student_tag = models.ManyToManyField(Tag,related_name = "student_tag")
    student_bio = RichTextField(blank = True)
    student_linkedin = models.URLField("Linkedin URL",blank = True)
    
    def __str__(self):
        return self.student_user.username