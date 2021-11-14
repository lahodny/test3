from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from log.models import Workout, WorkoutType


def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    workouts = Workout.objects.order_by('-date')

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'workouts': workouts
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)

class WorkoutCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Workout
    fields = ['name', 'date','workouttype']
    success_url = reverse_lazy('workouts')
    #login_url = '/accounts/login/'
    permission_required = 'log.add_race'