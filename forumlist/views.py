from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hw(request):
	context = {}
	return render(request,'home/homepage.html',context)