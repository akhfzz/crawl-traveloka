from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from time import sleep

class systemLogin():
    def __init__(self, driver, options):
        self.options=options
        self.driver=driver

    def login(self):
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-software-rasterizer")
        self.options.add_argument("-enable-webgl")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

        self.driver.get("https://www.tiket.com/")
        login = self.driver.find_element_by_xpath('//a[@class="header-right-item"]')
        login.click()
        self.driver.implicitly_wait(40)
        username = self.driver.find_element_by_xpath('//input[@name="username"]')
        username.send_keys("akhmadfaizal13@gmail.com")
        print("Email has been filled")
        submit_username = self.driver.find_element_by_xpath('//button[@class="btn-custom btn-custom-yellow btn-custom-full submitEmail"]')
        submit_username.click()
        self.driver.implicitly_wait(40)
        password = self.driver.find_element_by_xpath('//input[@name="password"]')
        password.send_keys("Kertosari23")
        submit_login = self.driver.find_element_by_xpath('//button[@class="btn-custom btn-custom-yellow btn-custom-full loginSubmitButton"]')
        submit_login.click()
        print("Login successfuly")
        self.driver.implicitly_wait(40)

    #not worked, need revision
    # def gain_cookie(driver):
    #     try:
    #         driver.implicitly_wait(15)
    #         verify = driver.find_element(by=By.XPATH, value='/html/body/div[8]/div/div[2]/div/div[2]/div/a')
    #         verify.click()
    #         print('\nCookies has saved')
    #         sleep(3)
    #     except NoSuchElementException:
    #         print('\nCookies hasnt saved')
    #         pass
    #     except TimeoutException:
    #         pass 
    #     except TimeoutError:
    #         print('Its so long time')
    #         pass