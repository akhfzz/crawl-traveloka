from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from time import sleep

def gain_cookie(driver):
    try:
        driver.implicitly_wait(15)
        verify = driver.find_element(by=By.XPATH, value='/html/body/div[8]/div/div[2]/div/div[2]/div/a')
        verify.click()
        print('\nCookies has saved')
        sleep(3)
    except NoSuchElementException:
        print('\nCookies hasnt saved')
        pass
    except TimeoutException:
        pass 
    except TimeoutError:
        print('Its so long time')
        pass

class systemLogin():
    def __init__(self, driver):
        # self.options=options
        self.driver=driver

    def login(self, email='akhfzz23@gmail.com', password='kertosari23'):
        # self.options.add_argument("start-maximized")
        # self.options.add_argument("disable-infobars")
        # self.options.add_argument("--disable-notifications")
        # self.options.add_argument("--headless")
        # self.options.add_argument("--disable-software-rasterizer")
        # self.options.add_argument("-enable-webgl")
        # self.options.add_argument("--no-sandbox")
        # self.options.add_argument("--disable-dev-shm-usage")
        # self.options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

        email_el = '//*[@id="username"]'
        password_el = '//*[@id="password"]'

        login_page='https://www.traveloka.com/en-id/'
        self.driver.get(login_page)
        print('Driver will opened...')
        self.driver.implicitly_wait(10)

        dropdown=self.driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/div/div[3]/div[2]/div[5]/div[1]/div')
        dropdown.click()

        email_field = self.driver.find_element(by=By.XPATH, value=email_el)
        email_field.send_keys(email)
        password_field = self.driver.find_element(by=By.XPATH, value=password_el)
        password_field.send_keys(password)
        print('Email & Password has been filled..')

        self.driver.find_element(by=By.XPATH,value='//*[@id="__next"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div/div/div/div[1]/div[3]/div[1]/div[2]/div').click()
        print('Login successfully')

        # gain_cookie(self.driver)
        sleep(100)
