# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "x"
PASSWORD = "x"

chrome_driver_path = Service("C:/Users/BC/Development/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()
driver.get("https://tinder.com/")

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="u-320325879"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]')
)).click()  # Click log in
time.sleep(0.5)
WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]')
)).click()  # Log in with FB

base_window = driver.window_handles[0]
log_in = driver.window_handles[1]

driver.switch_to.window(log_in)  # Swap to pop up
driver.maximize_window()

time.sleep(1.5)
WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')
)).click()  # Accept cookies
WebDriverWait(driver, 3).until(EC.presence_of_element_located(
    (By.ID, 'email')
)).send_keys(EMAIL)  # Input email
WebDriverWait(driver, 3).until(EC.presence_of_element_located(
    (By.ID, 'pass')
)).send_keys(PASSWORD)  # Input password
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input').click()  # Submit

driver.switch_to.window(base_window)  # Back to main page

time.sleep(5)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
)).click()  # Allow cookie tracking

time.sleep(0.5)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
)).click()  # Allow location tracking

try:
    time.sleep(1)
    driver.switch_to.alert.accept()  # Chrome allow location
except NoAlertPresentException:
    pass

time.sleep(1)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
)).click()  # Deny notifications
time.sleep(5)

while True:  # Loop reject
    time.sleep(1.5)
    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]').click()
    except NoSuchElementException:
        actions = ActionChains(driver)
        actions.send_keys(Keys.LEFT).perform()  # Swipe left
