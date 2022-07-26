TWITTER DIET ENGLISH APRIL 2020 DATASET
Collected by Yelena Mejova <yelena.mejova@gmail.com>

Tweets were collected using the Twitter Streaming API with keywords related to diet (in particular, "diet" keyword). The collection is constrained to tweets labeled by Twitter as being in English (en) language. For each day, data has a random sample of up to 10,000 tweets. It spans April 2020, capturing the first lockdowns of COVID-19 pandemic.

The JSON provided by Twitter has been parsed and the following columns are in the dataset (tab delimited):

#1  text
#2  id
#3  created_at
#4  place
#5  truncated
#6  is_quote_status
#7  retweeted
#8  favorite_count
#9  retweet_count
#10 geo
#11 lang
#12 hashtags
#13 retweeted_status_id
#14 retweeted_status_user_id
#15 retweeted_status_user_screen_name
#16 retweeted_extended_tweet
#17 posting user id
#18 posting user name
#19 posting user screen_name
#20 posting user followers_count
#21 posting user friends_count
#22 posting user favourites_count
#23 posting user listed_count
#24 posting user statuses_count
#25 posting user description
#26 posting user location
#27 posting user created_at
#28 posting user utc_offset

You can read in the data into Pandas data frame using code like this:

import csv
import pandas as pd
tweets = pd.read_csv("DATAFILE", sep="\t", lineterminator='\n', low_memory=False, quoting=csv.QUOTE_NONE, escapechar=None, header=None)

(substitute DATAFILE with name of the file)
