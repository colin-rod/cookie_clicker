from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()
# driver.get("https://www.amazon.de/-/en/CFI-1216A/dp/B0BRQCBK2W?ref_=Oct_d_Oct_d_ss_d_20904927031_2&pd_rd_w=GF2r9&content-id=amzn1.sym.26917e3c-85ac-4381-9b85-27bff6e99150&pf_rd_p=26917e3c-85ac-4381-9b85-27bff6e99150&pf_rd_r=5P446WPN7BKAG1EA5K1B&pd_rd_wg=n0cUb&pd_rd_r=9abeea99-191e-448b-8201-d4f9f9c18e13&pd_rd_i=B0BRQCBK2W")
#
# price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")
#
# search_bar = driver.find_element(By.NAME,value="field-keywords")
# print(search_bar.tag_name)
#
# product_title = driver.find_element(By.XPATH,value='//*[@id="productTitle"]')
# print(product_title.text)

driver.quit()