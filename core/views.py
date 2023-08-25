from django.shortcuts import render, redirect


from .models import *
from .forms import *
# Create your views here.

# SITE VIEWS
def index(request):
    posts = Post.objects.all().order_by('-id')

    context = {'posts':posts}
    return render(request, 'index.html', context)

def vacancy(request):

    context = {}
    return render(request, 'career.html', context)

def examTable(request):

    context = {}
    return render(request, 'examtable.html', context)

def testTable(request):

    context = {}
    return render(request, 'testtable.html', context)

def mealTable(request):

    context = {}
    return render(request, 'mealtable.html', context)

def tables(request):

    context = {}
    return render(request, 'tables.html', context)

def termCalendar(request):

    context = {}
    return render(request, 'calendar.html', context)

def admission(request):

    context = {}
    return render(request, 'admissionoverview.html',context)

def ourProgrammes(request):

    context = {}
    return render(request, 'programmes.html', context)

def congrats(request):

    return render(request, 'reception.html')

def jobApplication(request):
    form = applicationForm()
    if request.method == 'POST':
        form = applicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('congrats')
    
    context = {'form':form}
    return render(request, 'job.html', context)

