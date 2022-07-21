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
#17 id
#18 name
#19 screen_name
#20 followers_count
#21 friends_count
#22 favourites_count
#23 listed_count
#24 statuses_count
#25 description
#26 location
#27 created_at
#28 utc_offset

You can read in the data into Pandas data frame using code like this:

import csv
import pandas as pd
tweets = pd.read_csv("DATAFILE", sep="\t", lineterminator='\n', low_memory=False, quoting=csv.QUOTE_NONE, escapechar=None, header=None)

(substitute DATAFILE with name of the file)
