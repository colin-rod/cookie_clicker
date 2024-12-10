from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://secure-retreat-92358.herokuapp.com/")
search = driver.find_element(By.NAME,value="fName")
search.send_keys("Python")
search = driver.find_element(By.NAME,value="lName")
search.send_keys("LAst Python")
search = driver.find_element(By.NAME,value="email")
search.send_keys("python@new.com")
search.send_keys(Keys.ENTER)

#driver.quit()