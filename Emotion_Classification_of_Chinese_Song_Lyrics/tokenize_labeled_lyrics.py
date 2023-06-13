# -*- coding: utf-8 -*-
"""tokenize_lyrics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sIUEkMna65ASxsdxXGNlj7CPRtZl6-D-
"""

import pandas as pd
from ckiptagger import WS
from tqdm import tqdm

df = pd.read_csv('./data/cleaned_result.csv')
ws = WS("./data/data")
df['text2'] = df['text2'].astype(str)
new_ly = df['text2'].to_list()

from ckiptagger import data_utils
data_utils.download_data_url("./")

if __name__ == '__main__':
  token_list = []
  for text in tqdm(new_ly):
    tokens = ws([text])
    token_list.append(tokens)

  flatten_tokens = []
  for list_1 in token_list:
    for sublist in list_1:
      flatten_tokens.append(sublist)

  flatten_string = []

  for ft in flatten_tokens:
    st = ' '.join(ft)
    flatten_string.append(st)

  df['clean'] = flatten_string
  df.to_csv('./data/tokenized_labeled_lyrics.csv', index = False)


