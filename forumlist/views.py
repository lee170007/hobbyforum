from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostPage(TemplateView):
	template_name = 'home/homepage.html'

	def get(self, request):
		all_posts =  Post.objects.all()
		form = PostForm()
		context = {
			'all_posts' : all_posts,
			'form': form
		}
		return render(request,self.template_name,context)

	def post(self, request):
	    if request.method == 'POST':
	        form = PostForm(request.POST, request.FILES)
	        if form.is_valid():
	            post=form.save(commit=False)
	            post.user_id = self.request.user
	            form.save()
	            return HttpResponseRedirect(reverse('forumlist:hw'))
	    else:
	        form = PostForm()
	    return render(request, 'home/homepage.html', {
	        'form': form
	    })


class PostDetail(TemplateView):
	template_name = 'home/detail.html'

	def detail(request, post_id):
		post = get_object_or_404(Post, pk = post_id)
		return render(request,'home/detail.html',{'post' : post})


class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)