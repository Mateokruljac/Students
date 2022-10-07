from django.urls import path
from events.views import all_events, all_venues, create_events, create_venue, detail_event, update_event,delete_event, update_venue,delete_venue,booking,events_matching_your_tag
urlpatterns = [
   #events url 
   path("",all_events,name = "all_events"),
   path("add-event",create_events,name = "create_event"),
   path("detail/<event_id>",detail_event,name = "detail"),
   path("update/<event_id>",update_event,name ="update"),
   path("delete-event/<event_id>",delete_event,name ="delete_event"),
   path("detail/<id>/booking",booking,name = "booking"),
   path("matching-your-tag-events",events_matching_your_tag,name = "matching"),
   
   #venues url 
   path("create-venue",create_venue,name = "create_venue"),
   path("all-venues",all_venues,name = "all_venues"),
   path("update-venue/<venue_id>",update_venue,name = "update_venue"),
   path("delete-venue/<venue_id>",delete_venue,name ="delete_venue"),
   
               
               ]