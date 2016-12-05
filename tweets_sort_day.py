import sys
import operator
import requests
import json
import twitter
from time import sleep
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

twitter_consumer_key = 'uUf1fCQxmmFTIae8kpsyz7pUg'
twitter_consumer_secret = 'zfoT4uU9PnyqfXUbSAloJC9d3EUBrKVUx2Rk9xGV4En7T7SOLK'
twitter_access_token = '800436122002145280-CeUolhXA79K7D9isYyKjl95Jqwfev4R'
twitter_access_secret = 'OV7Kuahs1SiMGJc9hmXSu0zlsvxpuuPHNF3FA5BS2loAm'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

#files for data by day of week
mon = open('mon.txt', 'w')
tue = open('tue.txt', 'w')
wed = open('wed.txt', 'w')
thu = open('thu.txt', 'w')
fri = open('fri.txt', 'w')
sat = open('sat.txt', 'w')
sun = open('sun.txt', 'w')

line_break = '\n'

#list of random handles
#handle variable
#example handles = ['@codecademy', '@cnn', '@rock', '@nbc', '@cbs']
handles_file = open('handles_from_textisms.txt', 'r')
handles = [handle[:-1] for handle in handles_file.readlines()]
handles_file.close()


#iterate over list of handles to compile list of all statuses
statuses_master = []
for handle in handles: #RESET THIS TO NO INDEX AFTER DEBUG
    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=20, include_rts=False)
    statuses_master.append(statuses)
#print (statuses_master)

"""slicing statuses_master for debug"""
#statuses_master = statuses_master[:5]
#print ("status\n\n\n\n\n-----------------------",statuses_master)

#counts for each day of week for this handle
mon_count = 0
tue_count = 0
wed_count = 0
thu_count = 0
fri_count = 0
sat_count = 0
sun_count = 0

#all tweets separated by day of week
mon_tweets = []
tue_tweets = []
wed_tweets = []
thu_tweets = []
fri_tweets = []
sat_tweets = []
sun_tweets = []

"""ITERATE OVER STATUSES FOR EACH DAY OF WEEK"""

#Monday
for statuses in statuses_master:
    for status in statuses:
        if (status.lang =='en') and ("Created=Mon" in status.__repr__()) :
            print (status.text)
            mon_tweets.append(status.text)
            mon_count += 1
print ('Monday  ', mon_count, '\n\n')

#Tuesday
for statuses in statuses_master:
    for status in statuses:
        if (status.lang =='en') and ("Created=Tue" in status.__repr__()) :
            print (status.text)
            tue_tweets.append(status.text)
            tue_count += 1
print ('Tuesday  ', tue_count, '\n\n')

#Wednesday
for statuses in statuses_master:
    for status in statuses:
        if (status.lang =='en') and ("Created=Wed" in status.__repr__()) :
            print (status.text)
            wed_tweets.append(status.text)
            wed_count += 1
print ('Wednesday  ', wed_count, '\n\n')

#Thursday
for statuses in statuses_master:
    for status in statuses:
        if (status.lang =='en') and ("Created=Thu" in status.__repr__()) :
            print (status.text)
            thu_tweets.append(status.text)
            thu_count += 1
print ('Thursday  ', thu_count, '\n\n')

#Friday
for statuses in statuses_master:
    for status in statuses:
        if (status.lang =='en') and ("Created=Fri" in status.__repr__()) :
            print (status.text)
            fri_tweets.append(status.text)
            fri_count += 1
print ('Friday  ', fri_count, '\n\n')

#Saturday
for statuses in statuses_master:
    for status in statuses:
        if (status.lang =='en') and ("Created=Sat" in status.__repr__()) :
            print (status.text)
            sat_tweets.append(status.text)
            sat_count += 1
print ('Saturday  ', sat_count, '\n\n')

#Sunday
for statuses in statuses_master:
    for status in statuses:
        if (status.lang =='en') and ("Created=Sun" in status.__repr__()) :
            print (status.text)
            sun_tweets.append(status.text)
            sun_count += 1
print ('Sunday  ', sun_count, '\n\n')


mon.write(str(mon_tweets))
mon.close()
tue.write(str(tue_tweets))
tue.close()
wed.write(str(wed_tweets))
wed.close()
thu.write(str(thu_tweets))
thu.close()
fri.write(str(fri_tweets))
fri.close()
sat.write(str(sat_tweets))
sat.close()
sun.write(str(sun_tweets))
sun.close()
