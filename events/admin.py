from django.contrib import admin
from events.models import Student, Tag,Venue,Event

# Register your models here.
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(Student)