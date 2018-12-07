from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import DEFAULT_TIMEOUT


def wait_until_clickable(driver, location):
    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(expected_conditions.element_to_be_clickable(location))


def wait_until_invisible(driver, location):
    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(
        expected_conditions.invisibility_of_element(location)
    )


def wait_until_invisibility_located(driver, location):
    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(
        expected_conditions.invisibility_of_element_located(location)
    )


def wait_until_visibility_located(driver, location):
    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(location)
    )


def wait_until_presence_located(driver, location):
    WebDriverWait(driver, timeout=DEFAULT_TIMEOUT).until(
        expected_conditions.presence_of_element_located(location)
    )
