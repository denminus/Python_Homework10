# # -*- coding: utf-8 -*-
# """Homework10.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1KqUL9IjTK8IRO4jklZOHbpN3zQOsBmdz

# # Задание 44 

#  В ячейке ниже представлен код генерирующий DataFrame, 
#  которая состоит всего из 1 столбца. 
#  Ваша задача перевести его в one hot вид. 
#  Сможете ли вы это сделать без get_dummies?

# -import random

# lst = ['robot'] * 10

# lst += ['human'] * 10

# random.shuffle(lst)

# data = pd.DataFrame({'whoAmI'lst})

# data.head()
# """

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})  
print(pd.get_dummies(data))

data.loc[data['whoAmI'] == 'human', 'human'] = True
data.loc[data['whoAmI'] == 'robot', 'robot'] = True
print(data)