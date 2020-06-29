from django.shortcuts import render
from root.detect import Predict
from .forms import *
import urllib
# Create your views here. 
def home_view(request): 
    
    if request.method == 'POST':
<<<<<<< HEAD
        form = UserForm(request.POST, request.FILES) 
        image=Predict()
        if form.is_valid(): 
            form.save()
            x_ray_img=request.FILES['x_ray_img'] 
            result = image.predict(x_ray_img)

            return render(request,'root/result.html',{'result':result})
            # return redirect('result') 
=======
        form = UserForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save() 
            x_ray_img=request.FILES['x_ray_img']
            result = image.GetResult(x_ray_img)
            context={'result':result}
            return render(request,'root/result.html',context)
        # if form.is_valid(): 
        #     form.save()
        #     x_ray_img=request.FILES['x_ray_img']
        #     result = image.GetResult(x_ray_img)
        #     context={'result':result}
        #     return render(request,'root/result.html',context)
        #     # return redirect('result') 
>>>>>>> master
    else: 
        form = UserForm() 
        return render(request, 'root/index.html', {'form' : form}) 
  
  
# def success(request): 
#     result=detect()
#     return HttpResponse('successfully uploaded')

