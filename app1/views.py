from django.shortcuts import render

def operations(request):
    d={'a':12,'b':24,'c':36}
    return render(request,'operations.html',context=d)

