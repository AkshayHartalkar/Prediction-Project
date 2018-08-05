from django.urls import path,include
from . import views

app_name='LoginApp'

urlpatterns = [
    path('',views.loginpage,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('feedback/',views.feedback_view,name="feedback"),
]
