from django.shortcuts import render,HttpResponseRedirect
from usepanel.models import Signup
from django.contrib import messages
# Create your views here.
def aminHome(request):
    if request.method=='POST':
        given_name=request.POST['srh']
      
        if given_name:
                
                
            ser_course=Signup.objects.filter(name__icontains=given_name) 
                
            if ser_course:
                   
                return render(request,'admin/adminHome.html',{'les':ser_course})
            else:
                messages.warning(request,'No Result Found!')
                    
        else:
            return HttpResponseRedirect('/aminHome')
    stu=Signup.objects.all()

    return render(request,'admin/adminHome.html',{'stus':stu})