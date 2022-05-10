from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from authentication import systemLogin
from tasks import resourceSearch
from time import sleep

if __name__ == '__main__':
    try:
        detail_doc = "./result/result-data-crawl/hotel.csv"
        url_doc = "./result/result-url-crawl/hotel-Bandung.csv"
        options = Options()
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe', options=options)

        obj_l = systemLogin(driver, options)
        obj_r = resourceSearch(driver, options)
        obj_l.login()
        obj_r.keywordResult()

    except KeyboardInterrupt:
        print('You have pressed Ctrl+C button.')
        driver.close()
        print('Driver closed.')