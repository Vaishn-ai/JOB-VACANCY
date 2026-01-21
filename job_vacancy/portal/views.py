from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Job
from .forms import JobForm

# Create your views here.

def home(request):
    template_name = "portal/home.html"
    return render (request, template_name)

def create_job(request):
    form = JobForm()
    if request.method=='POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home_url')
    context = {'form' : form}
    template_name = "portal/form.html"
    return render (request, template_name, context)

def show_job(request):

    #by job type, location, salary range, date posted
    jobs = Job.objects.all()
    context = {'jobs' : jobs}
    template_name = 'portal/show.html'
    return render (request, template_name, context)




def update_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(instance=job)
    if request.method=='POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect ('show_url')
    context = {'form': form}
    template_name = "portal/form.html"
    return render (request, template_name, context)

def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    job.delete()
    return redirect ('show_url')

def info_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    context = {'job': job}
    template_name = "portal/info.html"
    return render (request, template_name, context)