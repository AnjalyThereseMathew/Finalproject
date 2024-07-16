from django.db import models
from django.contrib.auth.models import User

# from django.finalproject.finalone.forms import ProfileD
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def __str__(self):
        return self.user.username
    def add_friend(self,account):
        if not account in self.friends.all():
            self.friends.add(account)
            
    def removefriend(self,account):
        if account in self.friends.all():
            self.friends.remove(account)

    
class Friendship(models.Model):
    from_user = models.ForeignKey(User, related_name='friendships_initiated', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friendships_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(blank=True,default=True)

    class Meta:
        unique_together = ('from_user', 'to_user')
class User1(models.Model):
    friends=models.ManyToManyField(User,blank=True)
class Personaldetails(models.Model):
    ename=models.CharField(max_length=100)
    des=models.CharField(max_length=100)
    image=models.ImageField(upload_to='img')
    email=models.EmailField()
    age=models.IntegerField()
    phone=models.IntegerField()
    def __str__(self): 
        return self.ename
class friendrequest(models.Model):
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='touser')
    from_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='fromuser')
class friendrequest1(models.Model):
    to_user=models.ForeignKey(Personaldetails,on_delete=models.CASCADE,related_name='touser')
    from_user=models.ForeignKey(Personaldetails,on_delete=models.CASCADE,related_name='fromuser')
class Profile(models.Model):
    ename=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    des=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='img',null=True)
    coverpic=models.ImageField(upload_to='img',null=True)
    email=models.EmailField(null=True)
    age=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='fromuser11')
    to_user= models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='touser11')
    frndrqst=models.ManyToManyField(User,blank=True,related_name='frndrqst')
    post=models.ImageField(upload_to='img',null=True)
    post1=models.CharField(max_length=1000,null=True)
    class Meta:
        unique_together = ('from_user', 'to_user')

class Post(models.Model):
    image = models.ImageField(upload_to='posts/images/')
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='authorcheck')
    text = models.TextField(null=True)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments12', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes12', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def total_likes(self):
     return self.likes.count()
    
class Content(models.Model):
    coverpic=models.ImageField(upload_to='img')
class textbox(models.Model):
    post=models.CharField(max_length=1000)




    
class allusers(models.Model):
    allusername=models.ForeignKey(Personaldetails,on_delete=models.CASCADE,null=True)