from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
pages = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")

#pages.click()
#print(pages.text)

search = driver.find_element(By.NAME,value="search")
#print (search)
search.send_keys("Python")
search.send_keys(Keys.ENTER)

#driver.quit()