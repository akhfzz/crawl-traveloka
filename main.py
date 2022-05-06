from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from authentication import systemLogin
from tasks import resourceSearch, hotelResultSearch
import os
from time import sleep

from test import travelokaTest

if __name__ == '__main__':
    try:
        detail_doc = "./result/result-data-crawl/hotel.csv"
        url_doc = "./result/result-url-crawl/hotel-Bandung.csv"
        options = Options()
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')

        obj_f = systemLogin(driver)
        # obj_s = resourceSearch(driver, options)
        obj_m = hotelResultSearch(driver)
        obj_f.login()
        # obj_s.keywordResult()
        obj_m.crawlProccessLocal(url_doc, detail_doc)

    except KeyboardInterrupt:
        print('You have pressed Ctrl+C button.')
        driver.close()
        print('Driver closed.')