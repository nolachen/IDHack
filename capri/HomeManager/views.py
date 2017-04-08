from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

#homepage view - This is the function that will be called
#when the user requests the homepage
def HomePage(request):

    context = {} #no context
    return render(request,'home_manager/home.html', context)

