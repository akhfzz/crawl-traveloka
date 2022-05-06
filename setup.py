from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import os

def get_browser(driver=None, launch_on=None):
    if driver == 'Chrome':
        co = Options
        co.add_argument("--headless")
        co.add_argument("--disable-dev-shm-usage")
        co.add_argument("--no-sandbox")
        if launch_on == 'local':
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=co)
    
    print('Loading driver')
    return driver
