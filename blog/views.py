from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .models import SubscribedUsers
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))
