from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils import run_dogg

SITE = "https://jakdojade.pl/krakow/trasa/"
FROM_XPATH = "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[1]/div[2]/form/strong/input"
TO_XPATH = "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[2]/div[2]/form/strong/input"
SUGGEST_CLASSNAME = "cn-location-name"
RESULTS_CLASSNAME = "section-action-popup-container"
ACCEPT_BUTTON_CLASSES = "//div/div/div/div/div/button[2]"


def fill_input(driver, xpath, value):
    driver.find_element_by_xpath(xpath).send_keys(value)
    sleep(1)

    WebDriverWait(driver, timeout=3, ignored_exceptions=NoSuchElementException).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, SUGGEST_CLASSNAME))
    )

    # element = driver.find_element_by_class_name(SUGGEST_CLASSNAME)
    # WebDriverWait(driver, timeout=3, ignored_exceptions=NoSuchElementException).until(
    #     expected_conditions.visibility_of(element)
    # )
    element = driver.find_element_by_class_name(SUGGEST_CLASSNAME)
    element.click()


def submit_form(driver):
    WebDriverWait(driver, timeout=10).until(
        expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "cn-location-subname"))
    )

    driver.find_element_by_class_name("cn-planner-action-button").click()


def accept_cookies(driver):
    WebDriverWait(driver, timeout=10).until(
        expected_conditions.presence_of_element_located((By.XPATH, ACCEPT_BUTTON_CLASSES))
    )
    element = driver.find_element_by_xpath(ACCEPT_BUTTON_CLASSES)
    WebDriverWait(driver, timeout=10).until(
        expected_conditions.visibility_of(element)
    )
    element.click()


def fill_form_with_data(driver, start, destination):
    run_dogg()

    WebDriverWait(driver, timeout=10).until(
        expected_conditions.presence_of_element_located((By.XPATH, FROM_XPATH)))

    fill_input(driver, FROM_XPATH, start)
    fill_input(driver, TO_XPATH, destination)


def search_jakdojade(start, destination):
    driver = webdriver.Firefox(
        firefox_profile='/Users/mrapacz/Library/Application Support/Firefox/Profiles/fpgs4zbo.semantyka')
    driver.maximize_window()
    driver.get(SITE)

    accept_cookies(driver)
    fill_form_with_data(driver, start, destination)
    submit_form(driver)
