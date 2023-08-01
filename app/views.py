from django.shortcuts import render

# Create your views here.
def conditional(request):
     d={'a':20,'b':15}
     return render(request,'conditional.html',context=d)
