from http.client import HTTPResponse
import json
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import Registerform,PersonalD,ProfileD,textboxes,FriendRequestForm,textbox,PostForm,CommentForm
from .models import Like, Personaldetails,Comment,allusers,Profile,Content,textbox,friendrequest,User1,UserProfile,Friendship,Post
from django.contrib.auth.models import User
# Create your views here.
def requestsend(request,id):
    from_user=request.user
    to_user=User.objects.get(id=id)
    frndrequest,create=Friendship.objects.get_or_create(from_user=from_user,to_user=to_user)
    if create:
        # return render(request,'friendrequest.html')
        return HttpResponse('request send')
    else:
        return HttpResponse('request already sent')
    return render(request,'allfriends.html')
    # if request.method == 'POST':
    #     form = FriendRequestForm(request.POST)
    #     if form.is_valid():
    #         from_user = request.user
    #         to_user = Profile.get_object_or_404(User, id=id)
    #         Profile.objects.get_or_create(from_user=from_user, to_user=to_user)
    #         return redirect('/successfull', username=to_user.username)  # Redirect to the user's profile
    # else:
    #     form = FriendRequestForm()
    # return render(request, 'friendrequest.html', {'form': form})
# def requestaccept(request, *args, **kwargs):
# 	context = {}
# 	user = request.user
# 	if user.is_authenticated:
# 		user_id = kwargs.get("user_id")
# 		account = UserProfile.objects.filter(id=user_id)
# 		if account == user:
# 			friend_requests = Friendship.objects.filter(to_user=account, is_active=True)
# 			context['friend_requests'] = friend_requests
# 		else:
# 			return HttpResponse("You can't view another users friend requets.")
# 	else:
# 		redirect("login")
# 	return render(request, "friendrequest.html", context)
# def requestaccept(request, *args, **kwargs):
# 	user = request.user
# 	payload = {}
# 	if request.method == "GET" and user.is_authenticated:
# 		friend_request_id = kwargs.get("friend_request_id")
# 		if friend_request_id:
# 			friend_request = Friendship.objects.get(id=friend_request_id)
# 			# confirm that is the correct request
# 			if friend_request.to_user == user:
# 				if friend_request: 
# 					# found the request. Now accept it
# 					updated_notification = friend_request.accept()
# 					payload['response'] = "Friend request accepted."

# 				else:
# 					payload['response'] = "Something went wrong."
# 			else:
# 				payload['response'] = "That is not your request to accept."
# 		else:
# 			payload['response'] = "Unable to accept that friend request."
# 	else:
# 		# should never happen
# 		payload['response'] = "You must be authenticated to accept a friend request."
# 	return render(request,'friendrequest.html')

def requestaccept(request,Requestid):
    # acceptrequest=Profile.objects.all()
    acceptrequest = Friendship.objects.get(id=Requestid)
    # if acceptrequest.to_user == request.user:
    if request.user != acceptrequest.to_user:
        
      
        acceptrequest.to_user.friends.add(acceptrequest.from_user)
        
        acceptrequest.from_user.friends.add(acceptrequest.to_user)
        acceptrequest.delete()
        return HttpResponse('friend request accepted')
    else:
        return render(request,'friendrequest.html',{'acceptrequest':acceptrequest})



# Create your views here.
def loginPage(request):
     username=request.POST.get('usern')
     password=request.POST.get('passn')
    

     user=authenticate(request,username=username,password=password)
     if user:
          login(request,user)
          messages.success(request,'User has logged in')
         
          pro=Profile.objects.all()
          posts = Post.objects.all().order_by('-created_at')
          comment=Comment.objects.all().order_by('-created_at')
          like=Like.objects.all()
          return render(request,'afterlogin.html',{'pro':pro,'posts':post,'comment':comment})
     else:
         messages.add_message(
                request, messages.ERROR, "Incorrect username or password"
                )
         form = Registerform()
         return render(request,'homepage.html',{'form':form})
     return render(request,'homepage.html',{'anjal':'anjaly'})
# def profile(request,pk):
    
#      pk=request.pk
#      pro=Profile.objects.get(pk=pk)
#     #  pro=Profile.objects.get(pk=usr)
#      return render(request,'profile.html',{'pro':pro})
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def profile(request,id):
    
    if request.method == 'POST':
     form=textbox(request.POST,request.FILES)
     if form.is_valid():
         form.save()
        
         return render(request,'profile.html',{'form':form})
     else:
         form=textbox()
         my_data = Profile.objects.get(id=id)
         return render(request,'profile.html',{'my_data':my_data})

    my_data = Profile.objects.get(id=id)
    return render(request,'profile.html',{'my_data':my_data})
def post(request):
    
    if request.method == 'POST':
     form=textbox(request.POST,request.FILES)
     if form.is_valid():
         form.save()
        
         return render(request,'post.html')
    else:
     form=textbox()
    return render(request,'post.html',{'form':form})
def allfriends(request,id):
    # my_data = Profile.objects.all()
    # my_data1=User1.objects.all()
    # current_user_profile =UserProfile.objects.all()
    # friends = current_user_profile.friends.all()
    # all_users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    # non_friends = [user for user in all_users if user not in friends]
    current_user=request.user
    allusers = Profile.objects.exclude(id=id)
    # non_friends = [user for user in allusers].exclude(user in )
    # non_friends=User.objects.exclude(
    #     id__in=Profile.objects.filter(from_user=current_user).values('to_user_id')
    # ).exclude(id=current_user.id)
    # filter(id__in=Profile.objects.exclude(from_user=current_user)
    context = {
        'non_friends': allusers
    }
    
    
    form=FriendRequestForm()
        
    return render(request,'allfriends.html',context)

# def checkfunction(request):
#      if request.method == 'POST':
#       form=textboxes(request.POST,request.FILES)
#       if form.is_valid():
#          form.save()
        
#          return render(request,'header.html',{'form':form})
#      else:
#          form=textboxes()
#      return render(request,'profile.html',{'form':form})

    
def Personaldetails(request):
    if request.method == 'POST':
       form = PersonalD(request.POST, request.FILES)
    #    if form.is_valid():
    #            form.save()
    #            return render(request,'homepage.html',{'form':form})
       if form.is_valid():
            # a=form.s:ave(commit=False)
            # a.user=request.user
            # a.save()
            form.save()
            return render(request,'afterlogin.html')
    else:
     form=PersonalD()
     return render(request,'Personal.html',{'form':form})

  
def homepage(request):
    my_data = Profile.objects.all()
   
    return render(request,'homepage.html',{'my_data':my_data})

    
    # if request.method == "POST":
    #     form = Registerform()
    #     if form.is_valid():
    #         form.save()
    #         return redirect('dashboard_home')
    # site_profile = User.objects.get(username=request.user)
    form = Registerform()
    # form=Registerform.objects.get(username='username')
    # form=User.objects.all()
    return render(request,'homepage.html',{'form':form})
def homepagemain(request):
   
    
    pro=Profile.objects.all()
    return render(request,'afterlogin.html',{'pro':pro})
     
def success(request):
    return render(request,'homepage1.html')
def register(request):
   if request.method=='POST':
          form=Registerform(request.POST)
    
          ur=form.data['username']
          subject='Welcome to INSTABOOK'
          message=f'Welcome to INSTABOOK.You have successfully registered to INSTABOOK' 
          from_email=settings.EMAIL_HOST_USER
          z=form.data['email']
          to_mail=[z]
         
          if form.is_valid():
               form.save()
               send_mail(subject ,message ,from_email, to_mail,fail_silently=False)
               return redirect(success)
   else:
         form=Registerform()
   return render(request,'register1.html',{'form':form})

# def register1(request):
#     return render(request,'register1.html')


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    comment=Comment.objects.all().order_by('-created_at')
    like=Like.objects.all()
    return render(request, 'viewallpost.html', {'posts': posts,'comment':comment,'like':like})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'addcomment.html', {'form': form})

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('home')

def post_download(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_download.html', {'post': post})