from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


 
def test_verisini_cek():
    options = Options()
    options.headless = True
    global garanti_test
    global X_test
# =============================================================================
#     BIST100
# =============================================================================
    driver_path = r"..\geckodriver\geckodriver.exe"
    fox = webdriver.Firefox(options=options,executable_path=driver_path)
    url = "https://tr.investing.com/indices/ise-100-historical-data"
    fox.get(url)

    time.sleep(5)
    bist100_open = fox.find_element_by_xpath('//*[@id="curr_table"]/tbody/tr[2]/td[3]')
    bist100_open = bist100_open.get_attribute('innerHTML')
    fox.close()
# =============================================================================
#      Garanti Verilerinin Çekilmesi 
# =============================================================================
    browser = webdriver.Firefox(options=options,executable_path=driver_path)
    
    url = "https://finance.yahoo.com/quote/GARAN.IS/history?p=GARAN.IS"
    browser.get(url)
    
    time.sleep(10)
    
    garan_open = browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[2]/span')
    garan_high = browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[3]/span')
    garan_low = browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[4]/span')
    garan_close = browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[5]/span')
    garan_volume = browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[7]/span')
    
    garan_is = []
    garanti = [garan_open,garan_high,garan_low,garan_close,garan_volume]
    for i in garanti:
        garan_is.append((i.get_attribute('innerHTML')))
        
        
    browser.close()
# =============================================================================
#        Dolar Verilerinin Çekilmesi
# =============================================================================

    browser = webdriver.Firefox(options=options,executable_path=driver_path)
    url = "https://finance.yahoo.com/quote/TRY%3DX/history?p=TRY%3DX"
    browser.get(url)
    
    time.sleep(5)
    
    usd_try = browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[2]/span')
    
    dolar = usd_try.get_attribute('innerHTML')
    
    browser.close()

# =============================================================================
#       Petrol Verilerinin Çekilmesi
# =============================================================================

    browser = webdriver.Firefox(options=options,executable_path=driver_path)
    url = "https://tr.investing.com/commodities/crude-oil-historical-data"
    browser.get(url)
    
    time.sleep(5)
    
    ham_petrol = browser.find_element_by_xpath('//*[@id="curr_table"]/tbody/tr[2]/td[3]')
    
    petrol = ham_petrol.get_attribute('innerHTML')
    
    browser.close()

# =============================================================================
#     Verilerin Modele Sokulmadan Hazırlanması 
#     Eğitimde kullanılan veri sıralaması: <br>
#     Garan_Open, Garan_High, Garan_Low, Garan_Close, Garan_Volume, Bist_Open, Dolar_Open, Petrol_Open
# =============================================================================
    
    garan_is[-1] = garan_is[-1].replace(',', '')
    
    garanti_test = []
    for i in garan_is:
        garanti_test.append(float(i))


    bist100_open = bist100_open.replace('.','')
    bist100_open = bist100_open.replace(',','.')
    bist100_open= float(bist100_open)
    garanti_test.append(bist100_open)
    garanti_test.append(float(dolar))
    petrol = petrol.replace(',','.')
    garanti_test.append(float(petrol))
    garanti_np = np.asarray(garanti_test).reshape(-1,1)

    sc = StandardScaler()
    test = sc.fit_transform(garanti_np)
    
    
    
    X_test = test.reshape(test.shape[1], test.shape[0], 1)
    print('test verimiz:  ', garanti_test)
    return garanti_test, X_test 





