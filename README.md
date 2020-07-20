# Unfollow Instagram

A project to automate the unfollow on instagram, setting the user free of paid apps.

This project uses:

* Selenium
* Python

## How to use

Run this command:

```shell
cp .env.sample .env
```

And fill the .env file with your credentials.

Then, create one file with the list of usernames that you want to unfollow (each one separated by a new line) and put the name of the file on the .env file (the default is just `users`), and then the script will understand that exists a file with the name that you put on the .env file with the extension `.txt`.

Don't forgot to put the firefox driver on the path of your system (see this [link](https://github.com/mozilla/geckodriver/issues/1190))

Finally, run the command:

```shell
python main.py
```
