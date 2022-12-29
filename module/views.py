from django.shortcuts import render

# Create your views here.

# rendert die base.html
def index(request):
    return render(request, 'module/base.html')
    
