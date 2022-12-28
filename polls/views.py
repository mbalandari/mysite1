from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey guys! Welcome to polls!")
