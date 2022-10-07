from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .models import Event,Venue
from .forms import CreateEventForm, CreateVenueForm, UpdateEventForm, UpdateVenueForm
# Create your views here.

# def home (request):
#     return render(request,"core/home.html")


def all_events (request):
    events = Event.objects.filter().order_by("event_date")
    return render (request,"events/all_events.html",{"events":events})

def create_events(request):
    submitted = False
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.event_manager = request.user
            form.save()
            return HttpResponseRedirect("/add-event?submitted=True")
        else:
            return render(request,"events/create_event.html",{"form":form})
        
    else:
        form = CreateEventForm()
        if "submitted" in request.GET:
            submitted = True 
        
        return render (request,"events/create_event.html",{"form":form,"submitted":submitted})


def detail_event(request,event_id):
    event = get_object_or_404(Event,pk = event_id)    
    return render (request,"events/detail_event.html",{"event":event})
   

def update_event(request,event_id):
    updated = False
    if request.method == "POST":
       event = Event.objects.get(pk = event_id)
       form = UpdateEventForm(request.POST or None, instance=event)
       if form.is_valid():
           form.save(commit = False)
           form.event_manager = request.user
           form.save()
           return HttpResponseRedirect(f"/update/{event.id}?updated=True")
       else:
           messages.info(request,"Something went wrong. Please, try again!")
    
    else:
        event = Event.objects.get(pk = event_id)
        form = UpdateEventForm(request.POST or None, instance = event)
        if "updated" in request.GET:
            updated = True
        
        return render (request,"events/update_event.html",{"form":form,"updated":updated,"event":event})

def delete_event(request,event_id):
    event = Event.objects.get(pk = event_id)
    event.delete()
    return redirect ("all_events")

        

def create_venue(request):
    submitted = False
    if request.method == "POST":
        form = CreateVenueForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.venue_owner = request.user
            form.save()
            return HttpResponseRedirect("/create-venue?submitted=True")
        else:
            #something is went wrong! 
            return render (request,"venues/create_venue.html",{"form":form})    
    else: 
        form = CreateVenueForm()
        if "submitted" in request.GET:
            submitted = True
        return render (request,"venues/create_venue.html",{"form":form,"submitted":submitted})


#display all venues on the screen
def all_venues (request):
    venues = Venue.objects.all().order_by("venue_name")
    return render (request,"venues/all_venues.html",{"venues":venues})


def update_venue(request,venue_id):
    updated = False
    if request.method == "POST":
        venue = Venue.objects.get(pk = venue_id)
        form = UpdateVenueForm(request.POST or None,instance = venue)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(f"{venue.id}?updated=True")
        else:
            messages.info(request,"Something went wrong. Please, try again!") 
            return render(request,"venues/update_venue.html",{"form":form,"venue":venue})
    else:
       venue = Venue.objects.get(pk = venue_id)
       form = UpdateVenueForm(request.POST or None,instance = venue)
       if "updated" in request.GET:
           updated = True 
        
       return render (request,"venues/update_venue.html",{"form":form,"updated":updated})

def delete_venue(request,venue_id):
    if request.method == "POST":
       venues = Venue.objects.all()
       venue = get_object_or_404(Venue,pk = venue_id)
       venue.delete()
       return render (request,"venues/all_venues.html",{"venues":venues})
                  
    else:
        venue = get_object_or_404(Venue,pk = venue_id)
        return render (request,"venues/delete_venue.html",{"venue":venue})
    
def booking(request,id):
    events = Event.objects.all().order_by("event_date")
    if request.method == "POST":
        booking = False
        event = get_object_or_404(Event,id = request.POST["booking"])
        if event.event_booking.filter(id = request.user.id).exists():
           event.event_booking.remove(request.user)
           booking = False
           return HttpResponseRedirect(reverse("detail",args=([str(id)])))
        else:    
            event.event_booking.add(request.user)
            booking = True
            return HttpResponseRedirect(reverse("detail",args=([str(id)])))

    
def events_matching_your_tag(request):
    tags = [tg.name for tg in request.user.student.student_tag.all()]
    # test = Event.objects.all()
    # print("TEST",test)
    events_list = []
    for tag in tags:
       events_list.append(Event.objects.filter(event_tag__name = tag).order_by("event_date"))
    try:
        [events] = events_list
    except ValueError:
        messages.info(request,"Unfortunately, There are no events to match your interests! But you can look at the others.")
        return render (request,"events/matching_events.html")
    # print(f"Events: {events}")
    if events == "[]" or events == None: 
        messages.info(request,"Unfortunately, we don't have any events matching your tags!")
        return render (request,"events/matching_events.html")
    else:
        return render (request,"events/matching_events.html",{"events":events})