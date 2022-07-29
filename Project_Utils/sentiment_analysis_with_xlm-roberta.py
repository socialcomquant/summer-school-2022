'''
CSS 2nd Summer School - @KocUniversity
This code snippet is an example of how to run xlm-roberta-base-sentiment model.

Model Ref: https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment
Paper Ref: https://arxiv.org/abs/2104.12250

Make sure the following packages are installed on your environment;
pip install transformers
pip install sentencepiece

'''

from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

import pandas as pd
from tqdm.auto import tqdm
tqdm.pandas()

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def get_label(rank):
  if rank == 0:
    return 'negative'
  if rank == 1:
    return 'neutral'
  if rank == 2:
    return 'positive'

MODEL = f"cardiffnlp/twitter-xlm-roberta-base-sentiment"

tokenizer = AutoTokenizer.from_pretrained(MODEL, use_fast=False)
config = AutoConfig.from_pretrained(MODEL)

# With Pytorch
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)


def inference(text:str):
  #if you didnt normalize your text uncomment this line and model default preprocessing can handle
  #text = preprocess(text)
  encoded_input = tokenizer(text, return_tensors='pt')
  output = model(**encoded_input)
  scores = output[0][0].detach().numpy()
  scores = softmax(scores)

  # Print labels and scores
  rank = np.argmax(scores)
  result = get_label(rank)
  return result

df = pd.read_csv('PATH')

print('Sentiment Analysis started')
df['sentiment'] = df['text_column_name'].progress_apply(lambda x: inference(x))

# save dataframe for later
df.to_csv('PATH')
