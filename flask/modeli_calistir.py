# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:48:56 2020

@author: batuh
"""

import pickle

    
def trendbul(X_test, y_test):
    
    yukle = pickle.load(open("model_garanti_aznitelik_54.kayit", 'rb')) 
    y_tahmin = yukle.predict(X_test)
    print('tahmin edilen kapanış:', y_tahmin)
    
    if y_tahmin - y_test[3] > 0:
        trend = 'Garan.IS kağıdına parayı bas'
    else:
        trend = 'Garan.IS kağıdına parayı basma'
    return y_tahmin, trend
    

  
