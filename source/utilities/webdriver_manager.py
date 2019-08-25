from selenium import webdriver
from source.utilities import constants
from source.utilities.properties import ReadConfig


def start_browser(browser_name, url):
    chrome_caps = {"browserName": "chrome",
                   "platform": "windows"}
    driver = None
    if browser_name == "chrome" or browser_name == "Chrome":
        #driver = webdriver.Remote(command_executor="http://192.168.1.156:4444/wd/hub", desired_capabilities=chrome_caps)
        driver = webdriver.Chrome(executable_path=constants.CHROME_PATH)
        driver.maximize_window()

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=constants.FIREFOX_PATH)

    driver.get(url)
    driver.implicitly_wait(ReadConfig.get_implicit_wait())
    return driver



