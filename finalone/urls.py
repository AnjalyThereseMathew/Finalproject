from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns=[

path('loginpage',views.loginPage,name="login"),
path('homepagemain',views.homepagemain,name="loginmain"),
path('homepage',views.homepage),
# path('confirmregister',views.register1,name="register1"),
path('registerpage',views.register,name="register"),
path('successfull',views.success),
path('profile/<int:id>',views.profile,name="profile"),
path('Personaldetails',views.Personaldetails,name='personaldetails'),
path('sendrequest/<int:id>',views.requestsend,name='sendrequest'),
path('acceptrequest/<int:Requestid>',views.requestaccept,name='acceptrequest'),
path('findfriends/<int:id>',views.allfriends,name='allfriends'),
path('posts',views.post,name='posts'),
path('createpost',views.create_post,name='createpost'),
path('homie', views.home, name='home'),
 path('<int:pk>/download/', views.post_download, name='post_download'),
   
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('like/<int:post_id>/', views.like_post, name='like_post')
]

urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)