from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome('./drivers/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 30)

driver.get("https://www.traveloka.com/en-id/hotel/search?spec=02-05-2022.03-05-2022.1.1.HOTEL_GEO.103859.Bandung.2&userPreferences=TRAVEL_FOR_BUSINESS")

# try:
#     wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#onetrust-accept-btn-handler"))).click()
# except:
#     pass

size = driver.find_elements(By.XPATH, "//*[@id='desktopContentV3']/div/div[2]/div[2]/div[3]/div[2]/div[3]")
org_windows_handle = driver.current_window_handle
for i in range(len(size)):
    ele = driver.find_element(By.CLASS_NAME, 'tvat-hotelName')
    driver.execute_script("arguments[0].scrollIntoView(true);", ele)
    onclick = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'tvat-hotelName'))
    )
    onclick.click()
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[1])
    try:
        name = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div[5]/div[1]/div/div[3]/div/div[1]/div/div[1]/div/div[1]/h1"))).text
        print(name)
    except:
        pass
    # try:
    #     price = wait.until(EC.visibility_of_element_located((By.ID, "soloPrecio"))).text
    #     print(price)
    # except:
    #     pass
    driver.close()
    driver.switch_to.window(org_windows_handle)