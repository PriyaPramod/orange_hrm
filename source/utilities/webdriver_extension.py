from selenium import webdriver
from source.utilities import constants
from source.utilities.properties import ReadConfig


def start_browser(browser_name, url):
    driver = None
    if browser_name == "chrome" or browser_name == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        driver = webdriver.Chrome(options=options,
                        executable_path=constants.CHROME_PATH)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path=constants.FIREFOX_PATH)

    driver.get(url)
    driver.implicitly_wait(ReadConfig.get_implicit_wait())

    return driver