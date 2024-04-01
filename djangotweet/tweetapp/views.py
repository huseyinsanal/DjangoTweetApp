from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from tweetapp.forms import AddTweetForm

# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets" : all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

def addtweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        #tweet = models.Tweet(nickname,message)
        #tweet.save()

        models.Tweet.objects.create(nickname=nickname, message=message)

        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')
    
def addtweetbyform(request):
    if request.method == "POST":
        print(request.POST)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        form = AddTweetForm()
        return render(request,'tweetapp/addtweetbyform.html',context={"form":form})
