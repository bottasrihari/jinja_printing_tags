from django.shortcuts import render

# Create your views here.
def conditional(request):
     d={'name':'hari','age':24}
     return render(request,'conditional.html',context=d)
