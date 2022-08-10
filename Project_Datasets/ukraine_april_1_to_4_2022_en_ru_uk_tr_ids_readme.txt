TWITTER UKRAINE APRIL 1-4 DATASET
Collected by Yelena Mejova <yelena.mejova@gmail.com>

Tweets were collected using the Twitter Streaming API with keywords related to the Ukraine-Russian conflict. The collection is constrained to tweets labeled by Twitter as being in English (en), Russian (ru), Ukrainian (uk), and Turkish (tr) languages. For each day, a data has a sample of 10,000 tweets for each language. It spans April 1-4 2020, around https://en.wikipedia.org/wiki/Bucha_massacre

Due to the constraints by the Twitter Terms of Service, only the tweet IDs are provided. To download the actual tweets ("rehydrate" the dataset), use instructions from any of these pages:
https://github.com/DocNow/twarc
https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/#dehydrate
http://digitalcollecting.lib.virginia.edu/toolkit/docs/social-media/collect-tweets/
https://search.gesis.org/research_data/SDN-10.7802-1504?doi=10.7802/1504
https://towardsdatascience.com/learn-how-to-easily-hydrate-tweets-a0f393ed340e

The JSON provided by Twitter should then be parsed (I suggest the python json library), and the text field extracted, plus whatever fields you are interested in.
