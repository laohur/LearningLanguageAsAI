#  Mercari Price Suggestion Challenge          

https://www.kaggle.com/c/mercari-price-suggestion-challenge
需要下载数据文件


#### 记录如下           
(36689, 8)
   train_id  ...                                   item_description
0    972425  ...  Custom Bundle -1 Dark brown and 1 White Crossb...
1    127130  ...  Michael Kors Orange Leather Purse mint conditi...
2   1084030  ...  Color/ Pattern - Boysenberry Very padded area ...


#### 调参记录     
xgb
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
