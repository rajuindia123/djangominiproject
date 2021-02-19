from django.shortcuts import render,HttpResponseRedirect
from .forms import Signupform,Loginform,Infomationform
from django.contrib import messages
from .models import Signup,Infomation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentCurd
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def curd_api(request,pk=None):
   
    if request.method=='GET':
        id=pk
        if id is not None:
            stu=Infomation.objects.get(id=id)
            serializer=StudentCurd(stu)
            return Response(serializer.data)
        stu=Infomation.objects.all()
        serializer=StudentCurd(stu,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentCurd(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'messages':'Data Created'})
        return Response(serializer.errors)   
    if request.method=='PUT':
        id=pk
        stu=Infomation.objects.get(pk=id)
        serializer=StudentCurd(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'messages':'complete Data Updated'})
        return Response(serializer.errors)
    if request.method=='PATCH':
        id=pk
        stu=Infomation.objects.get(pk=id)
        serializer=StudentCurd(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'messages':'PartialData Updated'})
        return Response(serializer.errors)
    if request.method=='DELETE':
        id=pk
        stu=Infomation.objects.get(pk=id)
        stu.delete()
        return Response({'messages':'Data Deleted !'})



def home(request):
    if request.method == 'POST':
        fm=Signupform(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pn=fm.cleaned_data['phone_No']
            db=fm.cleaned_data['d_o_b']
            pw=fm.cleaned_data['password']
            co_pw=fm.cleaned_data['con_password']
            if pw==co_pw:
                # stu=Signup.objects.filter(stu_email=em)
                stu=Signup.objects.values('email').filter(email=em)

                exits=stu.exists()
                if exits==True:
                    messages.warning(request,'Email Id Already exists !')
                else:
                   
                    # request.session['user_email']=nm
                    reg=Signup(name=nm,email=em,password=pw,phone_No=pn,con_password=co_pw,d_o_b=db)
                    reg.save()
                    messages.success(request,'Register in Successfully!!')
                    messages.info(request,'Now you con Login !!')

                    fm=Signupform()
            else:
                messages.warning(request,'password and confirm does  not match !')
                fm=Signupform()
    else:
        fm=Signupform()
    return render(request,'users/signup.html',{'form':fm})

def loginuser(request):
    if request.method=='POST':
        fm=Loginform(request.POST)
        if fm.is_valid():
            le=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            stu=Signup.objects.values('email','password').filter(email=le,password=ps)
            exits=stu.exists()
            if exits==True:
                request.session['user_email']=le
                # messages.success(request,'Login in Successfully!!')
                fm=Loginform()
                return HttpResponseRedirect('/show_data')

            else:
                messages.warning(request,'Email and Password wrong')
    else:
        fm=Loginform()
    return render(request,'users/login.html',{'form':fm})


def show_data(request):
    if 'user_email' in request.session:
        email=request.session['user_email']
        # print(email)
        if request.method == 'POST':
            fm=Infomationform(request.POST)
            if fm.is_valid():
                nm=fm.cleaned_data['remark']
                # em=fm.cleaned_data['email']
            
                reg=Infomation(remark=nm,email=email)
                reg.save()
                messages.success(request,'Add in Successfully!!')
                fm=Infomationform()
        else:
            fm=Infomationform()
        

        data=Infomation.objects.all().filter(email=email)
        return render(request,'users/user_detail.html',{'form':fm,'stu':data})
    else:
        return HttpResponseRedirect('/')


# delete Data
def delete_data(request, id):
    if request.method == 'POST':
        pi= Infomation.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/show_data')

#Updatae Data
def update(request, id):
    if 'user_email' in request.session:
        if request.method == 'POST':
            pi=Infomation.objects.get(pk=id)
            fm=Infomationform(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/show_data')

        else:
            pi=Infomation.objects.get(pk=id)
            fm=Infomationform(instance=pi)

        return render (request,'users/updatedata.html',{'form':fm})
    else:
        return HttpResponseRedirect('/')
#Log Out
def logout(request):
    if 'user_email' in request.session:
        del request.session['user_email']
        return HttpResponseRedirect('/')


#API
def image(request):
    
    image_bgr = cv2.imread('1f15.jpg')
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    rectangle = (0, 56, 256, 150)
# Create initial mask
    mask = np.zeros(image_rgb.shape[:2], np.uint8)

# Create temporary arrays used by grabCut
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

# Run grabCut
    cv2.grabCut(image_rgb, # Our image
    mask, # The Mask
    rectangle, # Our rectangle
    bgdModel, # Temporary array for background
    fgdModel, # Temporary array for background
    5, # Number of iterations
    cv2.GC_INIT_WITH_RECT) # Initiative using our rectangle

# Create mask where sure and likely backgrounds set to 0, otherwise 1
    mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

# Multiply image with new mask to subtract background
    image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]
    # plt.imshow(image_rgb_nobg), plt.axis("off")
    # plt.show()
    return render (request,'users/image.html',{'form':image_rgb_nobg})

