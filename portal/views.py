from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Job
from .forms import JobForm, ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    template_name = "portal/home.html"
    return render (request, template_name)


def About(request):
    template = "portal/about.html"
    return render (request, template)

def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was successfully saved ✅")
            return redirect('contact_url')
    else:
        form = ContactForm()

    return render(request, "portal/contact.html", {"form": form})

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

    jobs = Job.objects.all()
    job = request.GET.get('job_type')
    location = request.GET.get('location')
    date_posted = request.GET.get('posted_date')
    salary = request.GET.get('salary_range')
    
    sort = request.GET.get('sort')

    if job:
        jobs = jobs.filter(job_type__icontains = job)
    if location:
        jobs = jobs.filter(location__icontains = location)
    if salary:
        jobs = jobs.filter(salary_range__icontains = salary)
    if date_posted:
        jobs = jobs.filter(posted_date = date_posted)
    if sort :
        jobs = jobs.order_by(sort)


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