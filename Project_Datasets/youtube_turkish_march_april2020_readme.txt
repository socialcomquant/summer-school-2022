TWITTER TURKISH YOUTUBE DATASET
Collected by Yelena Mejova <yelena.mejova@gmail.com>

Tweets were collected using the Twitter Streaming API with keywords "youtube" and "youtu.be". The collection is constrained to tweets labeled by Twitter as being in Turkish (tr) language. It spans March and April 2020.

The JSON provided by Twitter has been parsed and the following columns are in the dataset:

#1  text
#2  id
#3  created_at
#4  lang
#5  retweeted_status_id
#6  retweeted_status_user_id
#7  user_id
#8  user_name
#9  user_followers_count
#10 user_friends_count
#11 user_statuses_count
#12 user_location
#13 user_created_at
#14 youtube_ids

You can read in the data into Pandas data frame using code like this:

import csv
import pandas as pd
tweets = pd.read_csv("DATAFILE", sep="\t", lineterminator='\n', low_memory=False, quoting=csv.QUOTE_NONE, escapechar=None, header=None)

(substitute DATAFILE with name of the file)
