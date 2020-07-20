from time import sleep

from selenium.common.exceptions import NoSuchElementException

from constants import BASE_URL, BROWSER


def write_error(user):
    with open("errors.txt", "a+") as file:
        file.write(user + "\n")


def unfollow_button(xpath, user):
    sleep(2)
    try:
        unfollowButton = BROWSER.find_element_by_xpath(xpath)
        unfollowButton.click()
    except NoSuchElementException:
        write_error(user)
    sleep(2)


def unfollow(usernames):
    for user in usernames:
        BROWSER.get(f"{BASE_URL}/{user}/")
        unfollow_button(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span',
            user,
        )
        unfollow_button("/html/body/div[4]/div/div/div/div[3]/button[1]", user)
        sleep(4)
