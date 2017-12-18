from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserForm, LoginForm, ListingForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    #return render(request, 'member/login.html', context)
    messages.info(request, 'Logout successfully!')
    return HttpResponseRedirect(reverse('forumlist:hw'))

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # HERE AFTER LOGIN CAN GO TO SEE FORUM
                #albums = Album.objects.filter(user=request.user)
                #return render(request, 'member/index.html', {'albums': albums})
                messages.info(request, 'Login successfully!')
                return HttpResponseRedirect(reverse('forumlist:hw'))
            else:
                return render(request, 'member/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'member/login.html', {'error_message': 'Invalid login'})
    return render(request, 'member/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # HERE AFTER LOGIN CAN GO TO SEE FORUM
                #albums = Album.objects.filter(user=request.user)
                #return render(request, 'member/index.html', {'albums': albums}) 
                messages.info(request, 'Register and login successfully!')
                return HttpResponseRedirect(reverse('forumlist:hw'))
    context = {
        "form": form,
    }
    return render(request, 'member/register.html', context)

class ListingFormView(TemplateView):
    template_name = 'member/listing.html'

    # Display blank form
    def get(self, request):
        form = ListingForm()
        members = User.objects.all()
        args = {'form': form, 'members': members}
        return render(request, self.template_name, args)

class MemberList(APIView):

    def get(self, request):
        members = User.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        