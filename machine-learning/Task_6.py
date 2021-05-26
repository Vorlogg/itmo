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


# 6 РАЗДЕЛ (БЕЗ ПРОГРАММИРОВАНИЯ)
docs = ['президент рф дмитрий медведев предложить провести в ряд российский регион эксперимент по преподавание в школа основа религиозный культура история религия и основа светский этика',
        'президент россия дмитрий медведев предлагать серьёзно ужесточить ответственность пособник террорис',
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
