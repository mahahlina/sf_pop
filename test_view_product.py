from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()


def test_view_product_card(browser):
    browser.get("https://www.demoblaze.com/index.html")
    wait = WebDriverWait(browser, 10)
    product_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-title')))
    name_1 = product_name.text
    product_name.click()
    product_name_2 = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'name')))
    name_2 = product_name_2.text
    assert name_1 == name_2


def test_add_product_to_cart(browser):
    browser.get("https://www.demoblaze.com/index.html")
    wait = WebDriverWait(browser, 10)
    product_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-title')))
    name_1 = product_name.text
    product_name.click()
    add_to_cart = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Add to cart')))
    add_to_cart.click()
    cart = wait.until(EC.visibility_of_element_located((By.ID, 'cartur')))
    cart.click()
    name_2 = wait.until((EC.visibility_of_element_located((By.XPATH, "//*[@id='tbodyid']/tr/td[2]"))))
    name_2 = name_2.text
    assert name_1 == name_2


def test_purchase(browser):
    browser.get("https://www.demoblaze.com/index.html")
    wait = WebDriverWait(browser, 10)
    product_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-title')))
    product_name.click()
    add_to_cart = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Add to cart')))
    add_to_cart.click()
    cart = wait.until(EC.visibility_of_element_located((By.ID, 'cartur')))
    cart.click()
    browser.implicitly_wait(5)
    place_order = browser.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
    place_order.click()
    name = browser.find_element(By.ID, "name")
    name.send_keys("Test name")
    country = browser.find_element(By.ID, "country")
    country.send_keys("test country")
    city = browser.find_element(By.ID, "city")
    city.send_keys("test city")
    credit_card = browser.find_element(By.ID, "card")
    credit_card.send_keys("5565")
    month = browser.find_element(By.ID, "month")
    month.send_keys("March")
    year = browser.find_element(By.ID, "year")
    year.send_keys("2023")
    browser.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[10]/h2')))
    assert success_message.text == "Thank you for your purchase!"
