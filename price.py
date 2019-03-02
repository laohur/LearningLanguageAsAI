import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import math
from time import time
import datetime
from sklearn.model_selection import GridSearchCV

def rmsle(y, y_pred):
    assert len(y) == len(y_pred)
    to_sum = [(math.log(y_pred[i] + 1) - math.log(y[i] + 1)) ** 2.0 for i,pred in enumerate(y_pred)]
    return (sum(to_sum) * (1.0/len(y))) ** 0.5
#Source: https://www.kaggle.com/marknagelberg/rmsle-function

def get_data(dir):
    t=time()
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    train=pd.read_csv(dir+"train.tsv",sep='\t').fillna(" ")
    test=pd.read_csv(dir+"test.tsv",sep='\t').fillna(" ")
    print(train.shape)
    #print(train.head(3))
    print(test.shape)
    #print(test.head(3))
    print(" {0} 秒完成数据读入".format(time() - t))
    t=time()
    #此时归一化，tfidf会自私归一化，而且耗时很长
    x_train=train[["item_condition_id","shipping"]]
    #x_train = StandardScaler().fit_transform(x_train)
    x_train = pd.DataFrame(MinMaxScaler().fit_transform(x_train))
    x_test=test[["item_condition_id","shipping"]]
    #x_test = StandardScaler().fit_transform(x_test)
    x_test = pd.DataFrame(MinMaxScaler().fit_transform(x_test))
    y_train=train["price"]
    y_test=test["price"]
    print(" {0} 秒完成归一化".format(time() - t))
    t = time()
    print(x_train.shape)
    #print(x_train.head(3))

    # 不可四列一起训练，name band 太稀少了  不划算
    text_columns=["category_name","brand_name","name","item_description"]
    max_features=[1000,10000,20000,100000]
    tfidfer=[None]*4
    for i in range(4):
        tfidfer[i]=TfidfVectorizer(max_features=max_features[i],ngram_range=(1,1)).fit(train[text_columns[i]])
        a=tfidfer[i].transform(train[text_columns[i]])
        b=pd.DataFrame(a.toarray(),columns=tfidfer[i].get_feature_names())
        # print(tfidfer[i].get_feature_names())
        print(b.shape)
     #   print(b.head(3))
        x_train=x_train.join(b,rsuffix="_%d_"%(i))

        c=tfidfer[i].transform(test[text_columns[i]])
        d=pd.DataFrame(c.toarray(),columns=tfidfer[i].get_feature_names())
        x_test=x_test.join(d,rsuffix="_%d_"%(i))

    # print(x_train.head(3))
    print(x_train.shape)
    # print(x_test.head(3))
    print(x_test.shape)
    print(" {0} 秒完成tfidf".format(time() - t))
    t = time()

    return x_train,y_train,x_test,y_test

def model_predict(gen_model,x_train,y_train,x_test,y_test):
    t=time()
    print("开始训练"+gen_model.__name__)
    print(datetime.datetime.now())
    model=gen_model()
    model.fit(x_train,y_train)
    y_predict=model.predict(x_test)
    print("rmsle:%f" %rmsle(y_test,y_predict))
    print(datetime.datetime.now())
    print("训练结束")
    print(" {0} 秒耗时总计".format(time() - t))

def gen_xgb():
    # from xgboost.sklearn import XGBRegressor
    import xgboost as xgb
    params={"max_depth":3,"learning_rate":0.1,"n_estimators":30,"silent":0,"objective":"reg:linear"}
    model=xgb.XGBRegressor(**params)
    # model=xgb.XGBRegressor()
    # parameters = {'nthread':[4], #when use hyperthread, xgboost may become slower
    #               'objective':['reg:linear'],
    #               'learning_rate': [.03, 0.05, .07], #so called `eta` value
    #               'max_depth': [5, 6, 7],
    #               'min_child_weight': [4],
    #               'silent': [1],
    #               'subsample': [0.7],
    #               'colsample_bytree': [0.7],
    #               'n_estimators': [500]}

    # model = GridSearchCV(model,parameters,cv = 5,n_jobs = 5,verbose=True)

    # model.fit(x_train,y_train)
    # # print(model.best_score_)
    # # print(model.best_params_)
    # print(" {0} 秒完成xgb训练".format(time() - t))
    # y_predict=model.predict(x_test)
    # return y_predict
    return model
# def linear_predict:
# def rindge_predict:
# def lasso_predict:
# def dt_predict:
# def rf_predict:
# def svr_predict:
# def gmm_predict:

if __name__=="__main__":
    t0 = time()
    t = t0
    print("开始时间: ")
    print(datetime.datetime.now())
    dir = r"C:/Users/zen/code/Mercari Price Suggestion Challenge/data/"
    x_train,y_train,x_test,y_test=get_data(dir)
    # x_train,y_train,x_test,y_test=get_word2vec(dir)
    # x_train,y_train,x_test,y_test=get_brtt(dir)
    #y_predict=xgb_predict(x_train,y_train,x_test)
    gens=[gen_xgb]
    for gen in gens:
        model_predict(gen,x_train,y_train,x_test,y_test)
    # y_predict=xgb_model(x_train,y_train,x_test)
    # print("rmsle:%f" %rmsle(y_test,y_predict))
    # print(" {0} 秒耗时总计".format(time() - t))

from sklearn.ensemble import RandomForestRegressor
from gensim.models import Word2Vec
model = Word2Vec.load(x_train[""])

