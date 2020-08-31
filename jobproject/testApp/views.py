from django.shortcuts import render
from testApp.models import PuneJobs
def home_view(request):
    return render(request,'testApp/home.html')
def job_view(request):
    pune_job_list=PuneJobs.objects.all()
    my_dict={'pune_job':pune_job_list}
    return render(request,'testApp/punejob.html',context=my_dict)

# Create your views here.
