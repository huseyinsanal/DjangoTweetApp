from django.urls import path
from . import views


app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'),                                            #huseyinsanal.com/tweetapp/
    path('addtweet/', views.addtweet, name='addtweet'),                                     #huseyinsanal.com/tweetapp/addtweet
    path('addtweetbyform', views.addtweetbyform, name='addtweetbyform'),                    #huseyinsanal.com/tweetapp/addtweetbyform
    path('addtweetbymodelform', views.addtweetbymodelform,name='addtweetbymodelform'),      #huseyinsanal.com/tweetapp/addtweetbymodelform
]
