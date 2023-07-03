from django.shortcuts import render
from .models import OPD_Reg
from .forms import OPD_Reg_form
from django.contrib import messages

# Create your views here.
def Registration(request):
    form_data=OPD_Reg_form
    if request.method =='POST':
        form_data=OPD_Reg_form(request.POST)
        if form_data.is_valid():
            form_data.save()
            return render(request, 'OPD/Home.html')
            # messages.success(request, "Please Review Information Before Submit")
    return render(request,'OPD/Registration.html',{'form_data':form_data})


def update_and_review(request,pk):
    form = OPD_Reg.objects.get(pk=pk)
    if request.method=='POST':
        form= OPD_Reg_form(request.POST,instance=form)
        if form.is_valid():
            form.save()
            messages.success(request,"Information Saved Succesfully")
    return render(request, 'OPD/update_details.html',{'form': form})

def Navbar(r):
    return render(r,'OPD/Home.html')

def Data(r):
    Data =OPD_Reg.objects.all()

    return render(r,'OPD/Data.html',{'Data':Data})

def Home_page_layout(r):
    return render(r,'opd/Home_page.html')