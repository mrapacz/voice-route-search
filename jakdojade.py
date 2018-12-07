from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import FIREFOX_PROFILE_PATH, DEFAULT_TIMEOUT

FROM_XPATH = "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[1]/div[2]/form/strong/input"
TO_XPATH = "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[2]/div[2]/form/strong/input"


def fill_input(driver, xpath, value):
    navigation_suggestion = (By.CLASS_NAME, "cn-location-name")

    driver.find_element_by_xpath(xpath).send_keys(value)

    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT, ignored_exceptions=NoSuchElementException).until(
        expected_conditions.element_to_be_clickable(navigation_suggestion)
    )

    element = driver.find_element(navigation_suggestion)
    element.click()


def submit_form(driver):
    location_subname = (By.CLASS_NAME, "cn-location-subname")
    submit_button = (By.CLASS_NAME, "cn-planner-action-button")

    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(
        expected_conditions.invisibility_of_element_located(location_subname)
    )

    driver.find_element(submit_button).click()


def accept_cookies(driver):
    accept_button_location = (By.XPATH, "//div/div/div/div/div/button[2]")

    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(
        expected_conditions.presence_of_element_located(accept_button_location)
    )

    element = driver.find_element_by_xpath(accept_button_location)

    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(expected_conditions.visibility_of(element))
    element.click()


def fill_form_with_data(driver, start, destination):
    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(
        expected_conditions.presence_of_element_located((By.XPATH, FROM_XPATH)))

    fill_input(driver, FROM_XPATH, start)
    fill_input(driver, TO_XPATH, destination)


def search_jakdojade(start, destination):
    driver = webdriver.Firefox(firefox_profile=FIREFOX_PROFILE_PATH)
    driver.maximize_window()
    driver.get("https://jakdojade.pl/krakow/trasa/")

    accept_cookies(driver)
    fill_form_with_data(driver, start, destination)
    submit_form(driver)
