from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message, Comment, User

def my_wall(request):
    if "user_name" in request.session:

        context = {
            "all_msg" : Message.objects.all().order_by('-created_at'),
            "all_comment" : Comment.objects.all()
        }
        return render(request, "the_wall/wall.html", context)

    else:
        messages.info(request, "You must be logged in to enter the website")
        return redirect("/")

def create_message(request):
    if request.method == "POST":
        this_user = User.objects.get(id = request.session['user_id'])
        Message.objects.create(message = request.POST['text'], writer = this_user)

    return redirect("/wall")

def post_comment(request, msg_id):

    this_user = User.objects.get(id = request.session['user_id'])
    this_msg = Message.objects.get(id = msg_id)
    post = Comment.objects.create(comment = request.POST['comment'], post = this_msg, users = this_user)

    return redirect("/wall")

def delete_post(request, msg_id):

    this_msg = Message.objects.get(id = msg_id)
    if this_msg.writer.id ==  request.session['user_id']:
        this_msg.delete()
        return redirect("/wall")
    
    else:
        messages.error(request, "This message cannot be deleted")
        return redirect("/wall")
