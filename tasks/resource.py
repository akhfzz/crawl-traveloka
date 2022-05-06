from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from wf import file_writerow
import pandas as pd
import os
from time import sleep 

class resourceSearch():
    def __init__(self, driver, options):
        self.driver=driver
        self.options=options 
    
    def keywordResult(self):
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-software-rasterizer")
        self.options.add_argument("-enable-webgl")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        
        #btn #xpath bisa diganti sesuai keinginan
        
        self.driver.implicitly_wait(50)

        #submit #jika xpath btn diganti maka xpath search jg diganti
        search=self.driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[4]/div/div[1]/div/div/div[3]/div/div/div/div[5]/div[3]/div[5]')
        search.click()
        #jika eror berarti xpath hanya berguna saat non dialog pada laman

        self.driver.implicitly_wait(50)

        now_url = self.driver.current_url
        keyword_crawl= now_url.split('/')
        kategori = ''

        if len(keyword_crawl) > 6:
            kategori = keyword_crawl[4]
            keyword_city=keyword_crawl[5].split('.')
            filename=keyword_city[6]
            data = [kategori, now_url]
            file_writerow(f'./result/result-url-crawl/{kategori}-{filename}.csv', data)

        if len(keyword_crawl) == 6:
            kategori = keyword_crawl[4]
            keyword_destination=keyword_crawl[5].split('=')
            filename=keyword_destination[1]
            data=[kategori, now_url]
            file_writerow(f"./result/result-url-crawl/{kategori}-{filename}.csv", data)


        print("On progress, dataset has created")
        sleep(100)

