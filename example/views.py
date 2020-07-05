from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        print(request.POST['email'])
        print(request.POST['password'])
        d={'123456':'Your password is common',
           'admin':'you password easy to know',
           'your name':'hi your name',
           'password':'your password can not be taken',
           'hi':'Your password is not complex enough'}
        element=request.POST['password']
        if element in d:
            messages.error(request, d[element])
            return redirect('index')

        messages.info(request, 'This is the info message!')
        messages.error(request, 'ERROR! ERROR!')
        messages.success(request, 'You registered succesfully')
        messages.warning(request, 'Be careful!')
        
        return redirect('show_messages')

    return render(request, 'example/index.html')

def show_messages(request):
    return render(request, 'example/show_messages.html')