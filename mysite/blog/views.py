from django.http import HttpResponse

# Create your views here.

def index(request):

    data = {

        "Name" : "Tonessa Chatten",

        "Track" : "Backend(Python)",

        "Message" : "Hi, mentor, you're doing a great job & thank you for helping me!"

    }

    d = data.items()
 
    return HttpResponse(d)