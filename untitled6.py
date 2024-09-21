# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18BGZWX5q1lSYenLB0vtL5-W5zpPnxbjS
"""

!pip install gensim
from gensim.models import Word2Vec

sentence=("It's not only writers who can benefit from this free online tool. If you're a programmer who's working on a project where blocks of text are needed, this tool can be a great way to get that. It's a good way to test your programming and that the tool being created is working well.")

tokenized_sentence = [sent.split() for sent in sentence.lower().split('. ')]

model = Word2Vec(tokenized_sentence,min_count= 1)
model.wv.similar_by_word('to')