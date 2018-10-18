# -*- coding: utf-8 -*-
#  pip install python-twitter
import twitter
import re
from time import sleep
import random
import urllib2
import urllib
import sys
import datetime
import os

# Proxy user Only 
#proxy = 'http://192.168.0.46:8118'
#sproxy = 'https://192.168.0.46:8118'

# Getting proxy from evironement 

#os.environ['http_proxy'] = proxy
#os.environ['HTTP_PROXY'] = proxy
#os.environ['https_proxy'] = sproxy
#os.environ['HTTPS_PROXY'] = sproxy

consumerKey = os.environ['consumer_key']
consumerSecret = os.environ['consumer_secret']
accessTokenKey = os.environ['access_token_key']
accessTokenSecret = os.environ['access_token_secret']

def findTitle(url):
  headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0' }
  final_url = urllib2.urlopen(urllib2.Request(url)).geturl()
  req = urllib2.Request(final_url, None, headers)
  webpage = urllib2.urlopen(req).read()
  title = str(webpage).split('<title>')[1].split('</title>')[0]
  return title

def findcontent(url):
  content = []
  headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0' }
  final_url = urllib2.urlopen(urllib2.Request(url)).geturl()
  req = urllib2.Request(final_url, None, headers)
  webpage = urllib2.urlopen(req).read()
  content.append(webpage)
  title = str(webpage).split('<title>')[1].split('</title>')[0]
  content.append(title)
  return content

def findSource(url):
  headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0' }
  final_url = urllib2.urlopen(urllib2.Request(url)).geturl()
  req = urllib2.Request(final_url, None, headers)
  source = urllib2.urlopen(req).read()
  return source

if __name__ == '__main__':

   #title = findTitle("https://techcrunch.com/2017/10/28/new-seed-funds-pursue-ai-hard-tech-and-the-midwest/?utm_content=buffercbcca&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer")
   #print "========" + title
   hashtag = ""
   while True:
     api = twitter.Api(consumer_key=consumerKey, 
                       consumer_secret=consumerSecret,  
                       access_token_key=accessTokenKey, 
                       access_token_secret=accessTokenSecret
                      )
     list = api.GetListMembers(list_id='904980544005574656')
     for l in list:
       member = str(l.screen_name)
       User = api.GetUser(screen_name = member )
       statuses = api.GetUserTimeline(User.id, count=50)
   
       print(member)
       try:
         #trend = api.GetTrendsCurrent()
         hashtag = ["robot","cloud", "azure", "aws", "apple", "tesla", "uber" ," facebook ", "linux","fintech", "lifehacking" ,"google ", "docker", "devops", "bigdata", "datascience", "bitcoin", "IOT ", "AI ", "hack", "hacking", "lifestyle"]
           #print trend
       except twitter.error.TwitterError:
         print ("Get trend limited rate using default")
       for s in statuses:
         #print s.text
         urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', s.text)
         try:
           url = str(urls[0])
           content = findcontent(url)
           #print content
           source = content[0]
           title = content[1]
           #print urls
           print "--+" + url #+ " " + " --- " + source
         except:
           #print ('no url')
           continue
         #for t in trend:
         list_h = []
         for h in hashtag:
           try:
             #title = findTitle(url)
             #print "----> " + title
             #print u + ' ' +  t.name.decode("utf8").strip('#').lower() + ' not in ' + title.lower()
             if h.strip('#').lower() in title.decode("utf8").lower() or h.strip('#').lower() in title.decode("utf8").replace(" ", "").lower() or  h.strip('#').lower() in url.decode("utf8").lower() or h.decode("utf8").strip('#').replace(" ", "").lower() in source.decode("utf8").lower():
               list_h.append(h.replace(" ", ""))
               print " + " + h
               #Message =  "#"+ h.replace(" ", "") + " #fintech " + url + " " + title
             else:
               print "   " + h
              # print urllib2.urlopen(urllib2.Request(url)).geturl() + ' ' +  h.decode("utf8").strip('#').lower() + ' not in ' + title 
           except:
             e = sys.exc_info()[0]
             print (e)
             continue
         print list_h
         if len(list_h):
           Message = "#" +  " #".join(list_h) + " #fintech " + url + " "
           print "To be sent :--" + Message + "---"
           try:
             status = api.PostUpdate(Message)
             print (status.text)
             print str(datetime.datetime.now()) + ' =============-> OK sent ' + Message 
             #timer = random.randint(1200,1800)
             timer = random.randint(700,1111)
             print 'sleep waiting for another shot ' + str(timer)
             sleep(timer)
           except twitter.error.TwitterError as e:
             if str(e) == "[{u'message': u'You have already retweeted this tweet.', u'code': 327}]":
               print(e)
               continue                    
             elif str(e) == "[{u'message': u'Status is a duplicate.', u'code': 187}]":
               print ("Duplicated")
               continue
             elif str(e) == "[{u'message': u'Rate limit exceeded', u'code': 88}]":
               print ("Rate limit")
               print(e)
               print "Waiting 100 sec"
               sleep(100)
             elif str(e) == "[{u'message': u'User is over daily status update limit.', u'code': 185}]":
               print ("daily update limit")
               print(e)
               print "Waiting 200 sec"
               sleep(1800)
               continue
             elif str(e) == "[{u'message': u'Invalid or expired token.', u'code': 89}]":
               print ("Check Token")
               print(e)
               print "Waiting 200 sec"
               sleep(200)
               continue
             elif str(e) == "[{u'message': u'To protect our users from spam and other malicious activity, this account is temporarily locked. Please log in to https://twitter.com to unlock your account.', u'code': 326}]":
               print ("Account locked spam suspecion")
               print(e)
               print "Waiting 200 sec"
               sleep(200)
               continue
             else:
               print(e)
               continue
         else:
           print "no match found" 
