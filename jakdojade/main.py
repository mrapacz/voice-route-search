from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from config import FIREFOX_PROFILE_PATH
from jakdojade.locations import start_input_field, XPATHS, SITE, navigation_suggestion, location_subname, submit_button, \
    accept_button_location, START, DESTINATION
from jakdojade.wait import wait_until_clickable, wait_until_invisible, wait_until_presence_located, \
    wait_until_invisibility_located, wait_until_visibility_located


def fill_with_gps(driver, gps_button_location, loading_dots_location):
    wait_until_clickable(driver, gps_button_location)

    gps_button = driver.find_element(*gps_button_location)
    gps_button.click()

    wait_until_invisible(driver, loading_dots_location)


def fill_with_value(driver):
    wait_until_clickable(driver, navigation_suggestion)

    driver.find_element(*navigation_suggestion).click()


def fill_input(driver, start, value):
    input_field_location, gps_button_location, gps_loading_location = XPATHS[start]

    driver.find_element(*input_field_location).send_keys(value if value else " ")
    if value:
        fill_with_value(driver)
    else:
        fill_with_gps(driver, gps_button_location, gps_loading_location)


def submit_form(driver):
    wait_until_invisibility_located(driver, location_subname)

    driver.find_element(*submit_button).click()


def accept_cookies(driver):
    wait_until_visibility_located(driver, accept_button_location)
    driver.find_element(*accept_button_location).click()


def wait_for_form_to_load(driver):
    wait_until_presence_located(driver, start_input_field)


def fill_form_with_data(driver, start, destination):
    wait_for_form_to_load(driver)

    fill_input(driver, START, start)
    fill_input(driver, DESTINATION, destination)


def get_results(driver: webdriver.Firefox):
    result = By.XPATH, "/html/body/div[3]/main/div/ui-view/div/article/div[4]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/span[1]"

    wait_until_visibility_located(driver, result)
    return driver.find_element(*result).text


def search_jakdojade(start=None, destination=None, headless=True):
    options = Options()
    options.headless = headless

    driver = webdriver.Firefox(options=options, firefox_profile=FIREFOX_PROFILE_PATH)

    if not headless:
        driver.maximize_window()

    driver.get(SITE)

    accept_cookies(driver)
    fill_form_with_data(driver, start, destination)
    submit_form(driver)
    return get_results(driver)
