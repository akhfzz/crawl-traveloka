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
        while True:
            self.driver.get("https://m.tiket.com")
            self.driver.refresh()
            choice = str(input("Which product that want you do?: "))
            self.driver.implicitly_wait(60)

            if choice == 'pesawat':
                product = self.driver.find_element_by_xpath("//a[contains(@href, '/pesawat')]")
                self.driver.execute_script("arguments[0].click();", product)
                self.driver.implicitly_wait(60)
            elif choice == 'hotel':
                product = self.driver.find_element_by_xpath("//a[contains(@href, '/hotel')]")
                self.driver.execute_script("arguments[0].click();", product)
                self.driver.implicitly_wait(60)
            elif choice == 'kereta api':
                product = self.driver.find_element_by_xpath("//a[contains(@href, '/kereta-api')]")
                self.driver.execute_script("arguments[0].click();", product)
                self.driver.implicitly_wait(100)
            elif choice == 'to-do':
                product = self.driver.find_element_by_xpath("//a[contains(@href, '/to-do')]")
                self.driver.execute_script("arguments[0].click();", product)
                self.driver.implicitly_wait(100)
            elif choice == 'sewa mobil':
                product = self.driver.find_element_by_xpath("//img[@alt='Sewa Mobil']")
                product.click()
                self.driver.implicitly_wait(300)
                btn_click = self.driver.find_element_by_xpath("//button[@class='product-form-search-btn'")
                btn_click.click()

            self.driver.implicitly_wait(60)
            now_url = self.driver.current_url
            keyword_crawl= now_url.split('/')
            kategori = ''

            kategori = keyword_crawl[3]
            data=[kategori, now_url]
            file_writerow(f"./result/result-url-crawl/url-history.csv", data)
            print("On progress, dataset has created")

            self.driver.implicitly_wait(40)
            aggre = str(input("What you want crawl url more?(yes/no): "))
            if aggre == "yes":
                back = self.driver.find_element_by_xpath("//a[contains(@href, '/')]")
                self.driver.execute_script("arguments[0].click();", back)
            elif aggre == "no":
                self.driver.close()
            # sleep(100)

