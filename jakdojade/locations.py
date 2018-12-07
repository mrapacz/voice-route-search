from selenium.webdriver.common.by import By


def xpath(path):
    return By.XPATH, path


# cookies
accept_button_location = (By.XPATH, "//div/div/div/div/div/button[2]")

# input fields
start_input_field = xpath(
    "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[1]/div[2]/form/strong/input"
)

destination_input_field = xpath(
    "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[2]/div[2]/form/strong/input"
)

# gps
start_gps_button = xpath(
    "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[1]/div[2]/form/div[2]"
)

destination_gps_button = xpath(
    "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[2]/div[2]/form/div[2]"
)

start_loading_dots = xpath(
    "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[1]/div[2]/form/div[1]/main-loader-spinner/div/div"
)

end_loading_dots = xpath(
    "/html/body/div[3]/main/div/ui-view/div/article/div[2]/div/div[1]/div[2]/div[2]/form/div[1]/main-loader-spinner/div/div"
)

# suggestions
navigation_suggestion = (By.CLASS_NAME, "cn-location-name")

# form submission
location_subname = (By.CLASS_NAME, "cn-location-subname")
submit_button = (By.CLASS_NAME, "cn-planner-action-button")

START = "start"
DESTINATION = "destination"
XPATHS = {
    START: (start_input_field, start_gps_button, start_loading_dots),
    DESTINATION: (destination_input_field, destination_gps_button, end_loading_dots),
}

SITE = "https://jakdojade.pl/krakow/trasa/"
