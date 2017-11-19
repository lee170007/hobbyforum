from django.http import HttpResponse

# Create your views here.
def usrlogin(request):
	return HttpResponse("<h1>Member Login</h1>")