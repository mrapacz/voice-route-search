from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

FROM_XPATH = "(//input[@class='tactile-searchbox-input'])[1]"
TO_XPATH = "(//input[@class='tactile-searchbox-input'])[2]"
SUGGEST_CLASSNAME = "suggest"


def fill_input(driver, xpath, value):
    driver.find_element_by_xpath(xpath).send_keys(value)
    WebDriverWait(driver, timeout=1, ignored_exceptions=NoSuchElementException).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, SUGGEST_CLASSNAME))
    )
    if driver.find_elements(By.CLASS_NAME, "suggest"):
        driver.find_element_by_class_name("suggest").click()


def submit_form(driver):
    if not driver.find_elements(By.CLASS_NAME, "section-action-popup-container"):
        driver.find_element_by_xpath(TO_XPATH).submit()


def fill_form_with_data(start, destination):
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/maps/dir/")

    WebDriverWait(driver, timeout=10).until(
        expected_conditions.presence_of_element_located((By.XPATH, FROM_XPATH)))

    fill_input(driver, FROM_XPATH, start)
    fill_input(driver, TO_XPATH, destination)

    submit_form(driver)
