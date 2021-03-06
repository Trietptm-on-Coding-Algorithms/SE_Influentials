#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
CONSUMER_KEY =         'zcdo16CPPtdB24YyloeYtftua'
CONSUMER_SECRET =      'u3ZkR2CEnouRtoEF9y0Bl4Hsztb85T6Zsqqt33B3o3CN4NeVho'
ACCESS_TOKEN   =       '3220731312-bahpawZcvWFFEzZemSgpp7jnBj4NJkT8ud9BpfA'
ACCESS_TOKEN_SECRET =   'dv04c3AzBQlKKb4SS7Gl0RlMIVpIQFRbBUkDEPvlUZd81'

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('tweets/%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		#writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("stephenlrose")
