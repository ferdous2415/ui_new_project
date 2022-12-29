import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.google.com/")
driver.implicitly_wait(5)
driver.maximize_window()

signin = "//*[@id='gb']/div/div[2]/a"
email = "//*[@id='identifierId']"
next = "//*[@id='identifierNext']/div/button/span"

driver.find_element_by_xpath(signin).click()
driver.find_element_by_xpath(email).send_keys('ferdous2415@gmail.com')
time.sleep(2)
driver.find_element_by_xpath(next).click()


time.sleep(2)
driver.quit()