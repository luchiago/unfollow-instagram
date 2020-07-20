from constants import FILE_LOCATION
from login import login
from unfollow import unfollow


def read_file():
    with open(FILE_LOCATION, "r") as file:
        return [username.rstrip() for username in file.readlines()]

if __name__ == "__main__":
    usernames = read_file()
    login()
    unfollow(usernames)
