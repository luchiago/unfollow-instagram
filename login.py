from time import sleep

from selenium.webdriver.common.keys import Keys

from constants import BASE_URL, BROWSER
from settings import PASSWORD, TWO_FACTOR, USERNAME


def login():
    BROWSER.get(f"{BASE_URL}/accounts/login")
    sleep(5)
    _ = find_input_and_send_keys("username", USERNAME)
    passwordInput = find_input_and_send_keys("password", PASSWORD)
    passwordInput.send_keys(Keys.ENTER)
    if TWO_FACTOR:
        """
        If 2FA is enabled, the user
        will have time to put the code
        """
        sleep(30)
        find_not_now_button("/html/body/div[1]/section/main/div/div/div/div/button")
    # Notifications
    find_not_now_button("/html/body/div[4]/div/div/div/div[3]/button[2]")


def find_input_and_send_keys(name, key):
    element = BROWSER.find_element_by_name(name)
    element.send_keys(key)
    return element


def find_not_now_button(xpath):
    BROWSER.find_element_by_xpath(xpath).click()
