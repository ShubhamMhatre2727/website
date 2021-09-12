from django.shortcuts import render, HttpResponse
from home.models import Gym_Workout
# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def gym_workout(request):
    videos = Gym_Workout.objects.all()
    context = {
        'videos':videos
    }
    return render(request, 'gym_workout.html', context)