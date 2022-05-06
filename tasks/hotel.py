from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from wf import file_writerow, file_writerow_data
import pandas as pd
from time import sleep 

class hotelResultSearch():
    def __init__(self, driver):
        # self.options=options 
        self.driver=driver 
        self.wait = WebDriverWait(self.driver, 30)
    
    def crawlImage(self):
        try:
            element = '//*[@id="desktopContentV3"]/div/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/div/div[1]/div[1]/div/img'
            images= self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._2qd8A img'))).get_attribute('src')
            print("Image is crawled")
        except NoSuchElementException:
            print("Image has fail crawled")
            images=''
            pass 
        return images
    
    def crawlDestination(self):
        try:
            element = '//*[@id="desktopContentV3"]/div/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div'
            destination= self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._2qd8A div.tvat-hotelName'))).text
            print("Destination is crawled")
        except NoSuchElementException:
            print("Destination has fail crawled")
            destination=''
            pass 
        return destination
    
    def crawlPriceNormal(self):
        try:
            element = '//*[@id="desktopContentV3"]/div/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/div/div[1]/div[2]/div/div[2]'
            price=self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._2qd8A div.LR9Hv'))).text
            print("Price Normal is crawled")
        except NoSuchElementException:
            print("Price Normal has fail crawled")
            price=''
            pass 
        return price

    def crawlPriceHasDiscount(self):
        try:
            element = '//*[@id="desktopContentV3"]/div/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/div/div[1]/div[2]/div/div[2]'
            price= self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._2qd8A div.tvat-primaryPrice'))).text
            if price is None:
                print("No Discount here")
                pass
            print("Discount is crawled")
        except NoSuchElementException:
            print("Discount has fail crawled")
            price=''
            pass 
        return price

    def crawlLocation(self):
        try:
            element = '//*[@id="desktopContentV3"]/div/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/div/div[1]/div[1]/div/div/div[1]/div[1]/div[3]/span'
            location= self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._2qd8A span'))).text
            print("Location is crawled")
        except NoSuchElementException:
            print("Location has fail crawled")
            location=''
            pass 
        return location
    
    def crawlRating(self):
        try:
            element = '//*[@id="desktopContentV3"]/div/div[2]/div[2]/div[3]/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/meta'
            rating= self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._2qd8A meta'))).get_attribute('content')
            print("Rating is crawled")
        except NoSuchElementException:
            print("Rating has fail crawled")
            rating=''
            pass 
        return rating
    
    def crawlProccessLocal(self, url_doc, detail_doc):
        # self.options.add_argument("start-maximized")
        # self.options.add_argument("disable-infobars")
        # self.options.add_argument("--disable-notifications")
        # self.options.add_argument("--headless")
        # self.options.add_argument("-enable-webgl") 
        # self.options.add_argument("--no-sandbox") 
        # self.options.add_argument("--disable-dev-shm-usage")

        df = pd.read_csv(url_doc)
        resource=df['url']

        # for i in range(len(resource)):
            # self.driver.implicitly_wait(40)
        self.driver.get("https://www.traveloka.com/en-id/hotel/search?spec=02-05-2022.03-05-2022.1.1.HOTEL_GEO.103859.Bandung.2&userPreferences=TRAVEL_FOR_BUSINESS")
        self.driver.refresh()
        self.driver.implicitly_wait(40)

        try:
            image=self.crawlImage()
            destination=self.crawlDestination()
            priceNormal=self.crawlPriceNormal()
            priceDiscount=self.crawlPriceHasDiscount()
            rating=self.crawlRating()
            location=self.crawlLocation()

        except NoSuchElementException:
            # resource[i]=self.driver.get(self.driver.current_url)
            print("Resource moved")
        
        except TimeoutException:
            # print(f"Resource {resource[i]} should be move next url")
            print("Resource should be move next url")
            detail = [self.driver.current_url, '', '', '', '', '', '']
            # self.driver.get(resource[i+1])
        
        detail = [image, destination, priceNormal, priceDiscount, rating, location]
        print(image)
        file_writerow_data(detail_doc, detail)

        sleep(3600)

        print("Crawl successfully")
