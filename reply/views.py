from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Reply
from forumlist.models import Post
from .forms import ReplyForm
from .serializer import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages

# Create your views here.

class ReplyDetail(TemplateView):
	template_name = 'reply/reply_form.html'

	def get(self, request, post_id):
		post = get_object_or_404(Post, pk = post_id)
		form = ReplyForm()
		all_reply =  Reply.objects.filter(post_id=post_id).order_by('reply_date')
		context = {
			'post' : post,
			'form' : form,
			'all_reply' : all_reply
		}
		return render(request,self.template_name,context)

	def post(self, request,post_id):
	    if request.method == 'POST':
	        form = ReplyForm(request.POST, request.FILES)
	        post = get_object_or_404(Post, pk = post_id)
	        if form.is_valid():
	            reply=form.save(commit=False)
	            reply.user_id = self.request.user
	            reply.post_id = post
	            form.save()
	            messages.info(request, 'New reply added to post just now!')
	            return HttpResponseRedirect(reverse('reply:addreply',kwargs={'post_id':post_id}))
	    else:
	        form = ReplyForm()
	    return render(request, 'reply/reply_form.html', {
	        'form': form
	    })


class ReplyList(APIView):

    def get(self, request):
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)