#Mercari Price Suggestion Challenge

https://www.kaggle.com/c/mercari-price-suggestion-challenge



调参记录如下
C:\ProgramData\Anaconda3\python.exe "C:/Users/zen/code/Mercari Price Suggestion Challenge/full/full.py"
(36689, 8)
   train_id  ...                                   item_description
0    972425  ...  Custom Bundle -1 Dark brown and 1 White Crossb...
1    127130  ...  Michael Kors Orange Leather Purse mint conditi...
2   1084030  ...  Color/ Pattern - Boysenberry Very padded area ...

[3 rows x 8 columns]
(9173, 8)
   train_id  ...                                   item_description
0    166405  ...  Gently used. Like new. Credit card slots insid...
1    339244  ...                                 No description yet
2    858774  ...  Great condition - pebble gray/taupe leather co...

[3 rows x 8 columns]
 0.23186373710632324 秒完成数据读入
['backpack', 'bag', 'bags', 'baguette', 'cosmetic', 'crossbody', 'handbags', 'hobo', 'messenger', 'other', 'satchel', 'shoppers', 'shoulder', 'style', 'totes', 'women']
(36689, 16)
   backpack       bag  bags  baguette  ...  shoulder     style  totes     women
0  0.000000  0.000000   0.0       0.0  ...  0.000000  0.000000    0.0  0.459907
1  0.000000  0.564637   0.0       0.0  ...  0.564637  0.000000    0.0  0.538420
2  0.638096  0.000000   0.0       0.0  ...  0.000000  0.638096    0.0  0.385400

[3 rows x 16 columns]
(36689, 723)
    21  abercrombie  active  adidas  adrienne  ...  zac  zara  zeeland  zoe  zumba

[3 rows x 723 columns]
(36689, 6913)


[3 rows x 6913 columns]
(36689, 16758)

[3 rows x 16758 columns]
 30.069186210632324 秒完成tfidf

[3 rows x 24412 columns]
(36689, 24412)
C:\ProgramData\Anaconda3\lib\site-packages\sklearn\preprocessing\data.py:625: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.
  return self.partial_fit(X, y)
C:\ProgramData\Anaconda3\lib\site-packages\sklearn\base.py:462: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.
  return self.fit(X, **fit_params).transform(X)
   item_condition_id  shipping  backpack  ...  zulily  zumba_3_  zumiez_3_

[3 rows x 24412 columns]
(9173, 24412)
C:\ProgramData\Anaconda3\lib\site-packages\sklearn\preprocessing\data.py:625: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.
  return self.partial_fit(X, y)
C:\ProgramData\Anaconda3\lib\site-packages\sklearn\base.py:462: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.
  return self.fit(X, **fit_params).transform(X)
 168.33691835403442 秒完成归一化

Process finished with exit code -1

超过十分钟，手动停止

优化：归一化在tfidf之前

params={"max_depth":3,"learning_rate":0.1,"n_estimators":30,"silent":0,"objective":"reg:linear"}

手动停止
 305.25258231163025 秒完成xgb训练

params={"max_depth":3,"learning_rate":0.3,"n_estimators":10,"silent":0,"objective":"reg:linear"}
 rmsle:0.833887
392.82457637786865 秒耗时总计

params={"max_depth":6,"learning_rate":0.1,"n_estimators":30,"silent":0,"objective":"reg:linear"}
rmsle:0.754659
 944.513739824295 秒耗时总计

    tfidfer[i]=TfidfVectorizer(max_features=max_features[i],ngram_range=(1,2)).fit(train[text_columns[i]])
ngram_range1,2 内存不够
params={"max_depth":3,"learning_rate":0.1,"n_estimators":30,"silent":0,"objective":"reg:linear"}
rmsle:0.838636
 628.1802361011505 秒耗时总计# Mercari
