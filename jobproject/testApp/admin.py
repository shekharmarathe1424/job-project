from django.contrib import admin
from testApp.models import PuneJobs
class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
# Register your models here.
admin.site.register(PuneJobs,PuneJobsAdmin)
