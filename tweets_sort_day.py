import sys
import operator
import requests
import json
import twitter
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
handles = ['@codecademy', '@cnn', '@rock', '@nbc', '@cbs']

#iterate over list of handles to compile list of all statuses
statuses = []
for handle in handles:
    statuses.append(twitter_api.GetUserTimeline(screen_name=handle, count=20, include_rts=False))
print ((statuses))


#counts for each day of week for this handle
mon_count = 0
tue_count = 0
wed_count = 0
thu_count = 0
fri_count = 0
sat_count = 0
sun_count = 0

#Monday
for status in statuses:
  if (status.lang =='en') and ("Created=Mon" in status.__repr__()) :
    print (status.text)
    mon.write(str(status.text))
    mon.write(str(line_break))
    mon_count += 1
mon.close()
    
print ('Monday  ', mon_count, '\n\n')

#Tuesday
for status in statuses:
  if (status.lang =='en') and ("Created=Tue" in status.__repr__()) :
    print (status.text)
    tue.write(str(status.text))
    tue.write(str(line_break))
    tue_count += 1
tue.close()
    
print ('Tuesday  ', tue_count, '\n\n')

#Wednesday
for status in statuses:
  if (status.lang =='en') and ("Created=Wed" in status.__repr__()) :
    print (status.text)
    wed.write(str(status.text))
    wed.write(str(line_break))
    wed_count += 1
wed.close()
    
print ('Wednesday  ', wed_count, '\n\n')

#Thursday
for status in statuses:
  if (status.lang =='en') and ("Created=Thu" in status.__repr__()) :
    print (status.text)
    thu.write(str(status.text))
    thu.write(str(line_break))
    thu_count += 1
thu.close()
    
print ('Thursday  ', thu_count, '\n\n')

#Friday
for status in statuses:
  if (status.lang =='en') and ("Created=Fri" in status.__repr__()) :
    print (status.text)
    fri.write(str(status.text))
    fri.write(str(line_break))
    fri_count += 1
fri.close()
    
print ('Friday  ', fri_count, '\n\n')

#Saturday
for status in statuses:
  if (status.lang =='en') and ("Created=Sat" in status.__repr__()) :
    print (status.text)
    sat.write(str(status.text))
    sat.write(str(line_break))
    sat_count += 1
sat.close()
    
print ('Saturday  ', sat_count, '\n\n')

#Sunday
for status in statuses:
  if (status.lang =='en') and ("Created=Sun" in status.__repr__()) :
    print (status.text)
    sun.write(str(status.text))
    sun.write(str(line_break))
    sun_count += 1
sun.close()
    
print ('Sunday  ', sun_count, '\n\n')


