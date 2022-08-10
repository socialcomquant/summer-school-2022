TWITTER VACCINE TURKISH MARCH 2021 DATASET
Collected by Yelena Mejova <yelena.mejova@gmail.com>

Tweets were collected using the Twitter Streaming API with keywords related to vaccination (in Turkish and English). The collection is constrained to tweets labeled by Twitter as being in Turkish (tr) language. For each day, data has a random sample of up to 10,000 tweets. It spans March 2021, capturing the suspensions of AstraZeneca vaccine https://en.wikipedia.org/wiki/Oxford%E2%80%93AstraZeneca_COVID-19_vaccine#Suspensions .

Due to the constraints by the Twitter Terms of Service, only the tweet IDs are provided. To download the actual tweets ("rehydrate" the dataset), use instructions from any of these pages:
https://github.com/DocNow/twarc
https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/#dehydrate
http://digitalcollecting.lib.virginia.edu/toolkit/docs/social-media/collect-tweets/
https://search.gesis.org/research_data/SDN-10.7802-1504?doi=10.7802/1504
https://towardsdatascience.com/learn-how-to-easily-hydrate-tweets-a0f393ed340e

The JSON provided by Twitter should then be parsed (I suggest the python json library), and the text field extracted, plus whatever fields you are interested in.
