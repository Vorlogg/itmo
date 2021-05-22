import csv
from nltk.corpus import wordnet
from collections import Counter
import gensim
from gensim.models import KeyedVectors
# import textmining
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import scipy.spatial.distance as ds


# def get_hyponyms(synset):
#     hyponyms = set()
#     for hyponym in synset.hyponyms():
#         hyponyms |= set(get_hyponyms(hyponym))
#     return hyponyms | set(synset.hyponyms())
#
#
# # # csv.writer(open('output.txt', 'w+'), delimiter='\t').writerows(csv.reader(open("Task_4_sample_7.csv")))
# # synset = wordnet.synsets("journey")[0].name()
# # get_hyponyms(synset)
#
# journey = wordnet.synset('journey.n.01')
# # res = journey.hypernyms()
# res = journey.hyponyms()
# print(len(res))
# print(res[0])
# # gensim.models.KeyedVectors(5)
#

# tdm = textmining.TermDocumentMatrix()
#
# doc_1 = "президент рф дмитрий медведев предложить провести в ряд российский регион эксперимент по преподавание в школа основа религиозный культура история религия и основа светский этика"
# doc_2 = "президент россия дмитрий медведев предлагать серьёзно ужесточить ответственность пособник террорист"
# doc_3 = "дмитрий медведев активный пользователь интернет"
# doc_4 = "дмитрий медведев советовать чиновник считаться с блогосфера"
# doc_5 = "существовать ряд статистический метод для точный оценка тот насколько объект с разный свойство укладываться в тот или иной иерархия"
# doc_6 = "охватывать ряд независимый государство снг еэс"
#
# tdm.add_doc(doc_1)
# tdm.add_doc(doc_2)
# tdm.add_doc(doc_3)
# tdm.add_doc(doc_4)
# tdm.add_doc(doc_5)
# tdm.add_doc(doc_6)
#
# tdm.write_csv('matrix.csv', cutoff=1)
#
#
#
#
#
# 6 РАЗДЕЛ (БЕЗ ПРОГРАММИРОВАНИЯ)
docs = ['президент рф дмитрий медведев предложить провести в ряд российский регион эксперимент по преподавание в школа основа религиозный культура история религия и основа светский этика',
        'президент россия дмитрий медведев предлагать серьёзно ужесточить ответственность пособник террорист',
        'дмитрий медведев активный пользователь интернет',
        'дмитрий медведев советовать чиновник считаться с блогосфера',
        'существовать ряд статистический метод для точный оценка тот насколько объект с разный свойство укладываться в тот или иной иерархия',
        'охватывать ряд независимый государство снг еэс'
        ]
vec = CountVectorizer()
X = vec.fit_transform(docs)
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
# df.to_csv("tdm.csv", encoding="utf-8")
print(df[['дмитрий', 'медведев', 'ряд']])

vector_1 = np.array(df['дмитрий'])
vector_2 = np.array(df['медведев'])
vector_3 = np.array(df['ряд'])
print(vector_1)
print(vector_2)
print(vector_3)

print(ds.cosine(vector_1, vector_2))
print(ds.cosine(vector_1, vector_3))
#
#
#
#
#
