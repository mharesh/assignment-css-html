from django.shortcuts import render

# Create your views here.

def timetable(request):
    return render(request,'timetable.html')
def institute(request):
    return render(request,'institute.html')
def drink(request):
    return render(request,'drink.html')
def job(request):
    return render(request,'job.html')
def farmer(request):
    return render(request,'farmer.html')
def farmerdetails(request):
    return render(request,'farmerdetails.html')
def matrimonial(request):
    return render(request,'matrimonial.html')
def mocktest(request):
    return render(request,'mocktest.html')
def bootstrap(request):
    return render(request,'bootstrap.html')
def form(request):
    return render(request,'form.html')
def kmcustomform(request):
    return render(request,'kmcustomform.html')
def studenttable(request):
    return render(request,'studenttable.html')
def animations(request):
    return render(request,'animations.html')
def wrapper(request):
    return render(request,'wrapper.html')
def new(request):
    return render(request,'new.html')