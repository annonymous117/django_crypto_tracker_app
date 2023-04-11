
from django.contrib import admin
from django.urls import path,include
from .views import *
app_name="userapp"

urlpatterns = [
    path("",UserIndex,name="index"),
        path("userform",UForm,name="userform"),
        path("jsonres",TestjsonData,name="jsonres"),
        path("messageform",msgFormx,name="messageform"),
       path("test",Usertest,name="test"),
       path("userapp/",include('django.contrib.auth.urls')),
       path("usersform",UserMessage,name="usersform"),
       path("sendmessage",SendMessage,name="sendmessage"),
       path("gotohomepage",Gotohomepage,name="gotohomepage"),
       path("signup",SignUp,name="signup"),
       path("userapp/userlogout",UserLogout,name="userlogout"),
       path("userfeedback",UserFeedback,name='userfeedback'),
       path("usermail",Emailsender,name='usermail'),
       path("userapp/userfeedbackviews",UserFeedBackView,name='userfeedbacksviews'),
       path("usermailview",UsermailView,name='usermailview'),

    # path('admin/', admin.site.urls),
    # path("homepage",HomePage,name="homepage"),
    # path("user/<str:name>",Custom,name="user"),
    # path("Activity/<str:name>/<str:crypto>/<int:price>",Activity,name="user"),
    
]
