from django.shortcuts import render
from .detect import *
from .forms import *
# Create your views here. 
def home_view(request): 
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES) 

        if form.is_valid(): 
            form.save() 
            result = predict()
            context={'result':result}
            return render(request,'root/result.html',context)
            # return redirect('result') 
    else: 
        form = UserForm() 
        return render(request, 'root/index.html', {'form' : form}) 
  
  
# def success(request): 
#     result=detect()
#     return HttpResponse('successfully uploaded')

