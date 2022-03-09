from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import CreateView
from . models import *
#from . forms import *


# Create your views here.
def task_home(request):
    #task = Task.objects.all().order_by('-created')

    #search_query = request.GET.get('search',  '')

    #if search_query:
        #task = Task.objects.filter(Q(employee__icontains=search_query))

    template_name = 'home/card-statistics.html'
    context = {}

    return render(request, template_name, context)
