# Twitter-Python-Bot
<a href="http://bitly.com/2grT54q"><img src="https://cdn.codementor.io/badges/i_am_a_codementor_dark.svg" alt="I am a codementor" style="max-width:100%"/></a><a href="http://bitly.com/2grT54q"><img src="twitterbot.png" height="50">[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/HAAW)



Description : A Twitter bot to crawl intressting tweet about new tech and seek the posted urls in depth 

HOW It WORKS
================
The configuration is inside the python script : 

Requierements
================
1 - Installing the dependencies
```bash
pip install -r requirements.txt 
```
2- Adding Twitter API Credential

Installation
================

Add API TOKENS in environment and trigger the script.

```python
consumerKey = os.environ['consumer_key']
consumerSecret = os.environ['consumer_secret']
accessTokenKey = os.environ['access_token_key']
accessTokenSecret = os.environ['access_token_secret']

```
Before use
================
You'll need to add list of the people you follow, and get the List id 

```python
# ...
  list = api.GetListMembers(list_id='904980544005574656')
     for l in list:
# ...
```
Updating the hashTag 
================
You can customize the hashtag that you need by fullfulling the follow list :

```python
# ...
         hashtag = ["robot","cloud", "azure", "aws", "apple", "tesla", "uber" ," facebook ", "linux","fintech", "lifehacking" ,"google ", "docker", "devops", "bigdata", "datascience", "bitcoin", "IOT ", "AI ", "hack", "hacking", "lifestyle"]
# ...
```
Caution 
================
Unless you have a business account twitter will apply a daly quota / monthly quota : 
Please refer to twitter error table : 
```python
# ...
except twitter.error.TwitterError as e:
# ...
```
