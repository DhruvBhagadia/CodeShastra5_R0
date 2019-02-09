from django.shortcuts import render, HttpResponse
import tweepy
from newsapi import NewsApiClient
import json

# Create your views here.

def index(request):

    # get_tweets()
    # get_news("demonetization india")

    return render(request, 'index.html', {})


def linechart(request):

    return render(request, 'linechart.html', {})


def get_news(request):
    topic = "demonetization india"
    api = NewsApiClient(api_key="4e6941abb75c490a950e634acf91ed08")
    all_articles = api.get_everything(q=topic, language='en', sort_by='relevancy')
    publishers_list = {}
    for article in all_articles["articles"]:
        if article["source"]["name"] not in publishers_list:
            publishers_list[article["source"]["name"]] = {"url": "", "content": ""}
            publishers_list[article["source"]["name"]]["url"] =  article["url"]


    # parsed = json.loads(json.dumps(all_articles))
    return HttpResponse(json.dumps({'articles': publishers_list}), content_type="application/json")


def get_tweets(topic):

    consumer_key = 'K8rDGMdTDwKz2tWpNIuurZSr7'
    consumer_secret = 'wb1ZWvuC9loX78f6GVDVgNzoG0YATKLhPwjtXlnWrOiplm901u'
    access_token = '962553243116204032-XWr3Ud2mD56izQFWFXu2aZMCZ9MkGxZ'
    access_token_secret = 'fqYgYnEAkwy15NZBHhjb0ZCoL67hybGZe7fni8QXFL2RY'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    # public_tweets = api.home_timeline()
    # search_tweets = api.search(q=topic, lang="en")
    # for tweet in search_tweets:
    #     print(tweet.text)

    trends = api.trends_available()
    parsed = json.loads(json.dumps(trends))

    for trend in parsed:
        if trend["name"] == "Mumbai":
            place_id = trend["woeid"]
            print("Mumbai: ", place_id)
            trends_place = api.trends_place(place_id)
            place_parsed = json.loads(json.dumps(trends_place))
            place_parsed = json.dumps(place_parsed, indent=4, sort_keys=True)
            print(place_parsed)

def chart(request):
	data = [
				["China", 1882, "#7474F0"],
				["Japan", -33.923036, "#C5C5FD"],
				["Germany", -34.028249, "#952FFE"],
				["UK", -33.80010128657071, "#7474F0"]
			]
	context = {"data": data}
	return render(request, 'linechart.html', context)

def trying(request):
	return render(request, 'trying.html', {})

def render_sports_page(request):
	return render(request, 'sports.html', {})

def render_politics_page(request):
	return render(request, 'politics.html', {})
