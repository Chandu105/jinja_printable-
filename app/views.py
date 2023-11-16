from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='this is an assumption data'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)
def login(request):
    d={'username':'chandana','course':'python fullstack'}
    return render(request,'login.html',context=d)
