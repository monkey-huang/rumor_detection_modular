# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:03:41 2019

@author: huangxing
"""

# 引入 numpy、pd 和 sklearn(scikit-learn) 模組
import numpy as np
import pandas as pd
from sklearn import datasets
# 引入 train_test_split 分割方法，注意在 sklearn v0.18 後 train_test_split 從 sklearn.cross_validation 子模組搬到 sklearn.model_selection 中
from sklearn.model_selection import train_test_split
# 引入 KNeighbors 模型
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

# 引入 iris 資料集
raw_iris = datasets.load_iris()
# 探索性分析 Exploratory data analysis，了解資料集內容
# 先印出 key 值，列出有哪些值：['data', 'target', 'target_names', 'DESCR', 'feature_names']
print(raw_iris.keys())

# 印出 feature 值
print(raw_iris['data'])
# 印出目標值，分別對應的是三種花的類別：['setosa 山鳶尾' 'versicolor 變色鳶尾' 'virginica 維吉尼亞鳶尾']
print(raw_iris['target'])
# 印出目標標籤，三種花的類別：['setosa' 'versicolor' 'virginica']
print(raw_iris['target_names'])
# 印出資料集內容描述
print(raw_iris['DESCR'])
# 印出屬性名稱，['sepal length 花萼長度 (cm)', 'sepal width 花萼寬度 (cm)', 'petal length 花蕊長度 (cm)', 'petal width 花蕊寬度 (cm)']
print(raw_iris['feature_names'])

# 類別種類
print(np.unique(raw_iris.target))

