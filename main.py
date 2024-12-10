from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

def buy_upgrade(driver, item_list):
    cookie_count = get_cookie_count(driver)
    affordable_upgrades = {}
    for cost, id in item_list.items():
        if cookie_count > cost:
            affordable_upgrades[cost] = id
    print(affordable_upgrades)
    highest_price_affordable_upgrade = max(affordable_upgrades) if affordable_upgrades else None
    print(highest_price_affordable_upgrade)
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade] if highest_price_affordable_upgrade is not None else None

    driver.find_element(by=By.ID, value=to_purchase_id).click()

def get_cookie_count(driver):
    money_element = driver.find_element(By.ID, value="money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")
    cookie_count = int(money_element)
    print(cookie_count)
    return cookie_count

def continuous_clicking(cookie):
    """
    Continuously clicks the cookie
    """
    while True:
        cookie.click()


def get_item_list(driver,items):
    all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    item_prices = []

    # Convert <b> text into an integer price.
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    # Create dictionary of store items and prices
    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = items[n]
    return cookie_upgrades

def get_cookies_per_second(driver):
    cookies_per_second = driver.find_element(By.CSS_SELECTOR, value="#cps")
    print(cookies_per_second.text)

def main():
    # Setup WebDriver
    driver = webdriver.Firefox()
    driver.get("http://orteil.dashnet.org/experiments/cookie/")

    # Find the cookie element
    cookie = driver.find_element(By.ID, value="cookie")

    item_list = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    items = [item.get_attribute("id") for item in item_list]

    # Create threads for continuous clicking and periodic function
    click_thread = threading.Thread(target=continuous_clicking, args=(cookie,), daemon=True)
    click_thread.start()

    # Periodic function execution
    while True:
        time.sleep(5)
        item_list = get_item_list(driver,items)
        buy_upgrade(driver, item_list)
        get_cookies_per_second(driver)

if __name__ == "__main__":
    main()