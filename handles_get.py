from __future__ import print_function
import twitter

#100 handles from Demple.csv from textisms assignment
top_handles = open('handles_from_textisms.txt', 'r')
top_handles = [line.split(',') for line in top_handles.readlines()]

twitter_consumer_key = 'uUf1fCQxmmFTIae8kpsyz7pUg'
twitter_consumer_secret = 'zfoT4uU9PnyqfXUbSAloJC9d3EUBrKVUx2Rk9xGV4En7T7SOLK'
twitter_access_token = '800436122002145280-CeUolhXA79K7D9isYyKjl95Jqwfev4R'
twitter_access_secret = 'OV7Kuahs1SiMGJc9hmXSu0zlsvxpuuPHNF3FA5BS2loAm'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

#master list of handles
master_handles = []

#get friends of top_handles (bottom_handles)
print (top_handles[0][0])
for handle in top_handles:
    friends = twitter_api.GetFriends(screen_name=handle[0])
    for friend.screen_name in friends:
        master_handles.append(friend.screen_name)
    print ([friend.screen_name for friend in friends])

#print([u.screen_name for u in users])
