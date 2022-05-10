from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("start-maximized")
# options.add_argument("--headless")
options.add_argument("-enable-webgl") 
options.add_argument("--no-sandbox") 

driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe', options=options)
driver.get("https://www.tiket.com/")
login = driver.find_element_by_xpath('//a[@class="header-right-item"]')
login.click()
driver.implicitly_wait(40)
username = driver.find_element_by_xpath('//input[@name="username"]')
username.send_keys("akhmadfaizal13@gmail.com")
print("Email sudah di isi")
submit_username = driver.find_element_by_xpath('//button[@class="btn-custom btn-custom-yellow btn-custom-full submitEmail"]')
submit_username.click()
driver.implicitly_wait(40)
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys("Kertosari23")
submit_login = driver.find_element_by_xpath('//button[@class="btn-custom btn-custom-yellow btn-custom-full loginSubmitButton"]')
submit_login.click()
print("Login berhasil")
driver.implicitly_wait(40)
driver.get('https://www.tiket.com/pesawat/search?d=JKTC&a=SUBC&dType=CITY&aType=CITY&date=2022-05-10&adult=1&child=0&infant=0&class=economy&flexiFare=false')
ele = driver.find_elements_by_xpath('//div[@class="list-horizontal__middle"]/div[@class="text-time"]')
for i in range(len(ele)):
    print(ele[i].text)

driver.implicitly_wait(200)