import requests
from bs4 import BeautifulSoup
import re
from textblob import TextBlob

# page = requests.get("https://www.greaterkashmir.com/article/news.aspx?story_id=312278&catid=12&mid=53&AspxAutoDetectCookieSupport=1")
page = requests.get("https://www.forbes.com/sites/meghabahree/2019/01/28/media-billionaire-subhash-chandra-battles-to-regain-control-of-his-empire/")

soup = BeautifulSoup(page.content, 'html.parser')

p_tag = soup.find_all('p')

p = ""
if len(p_tag) > 0:
    for i in p_tag:
        p += i.get_text()

print(TextBlob(p).sentiment.polarity)
