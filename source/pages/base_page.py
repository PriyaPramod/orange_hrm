from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from source.utilities.properties import ReadConfig


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(ReadConfig.get_explicit_wait())
        self.wait = WebDriverWait(driver, ReadConfig.get_explicit_wait())

    def find_element(self, by, value):
        try:
            web_element = self.driver.find_element(by, value)
            return web_element
        except NoSuchElementException:
            print("Exception: element not found: \n "+" Locator type: ", by, " Locator value: "+value)
            assert False

    @staticmethod
    def send_keys(web_element, value_to_type):
        try:
            web_element.send_keys(value_to_type)
        except Exception:
            print("Unable to type the value to text box "+Exception)
            assert False

    @staticmethod
    def click(web_element):
        try:
            web_element.click()
        except Exception:
            print("Unable to click on the element: "+Exception)
            assert False

    def verify_title(self, expected_title):
        flag = False
        try:
            flag = self.wait.until(ec.title_contains(expected_title), "Application is not navigated to the: " + expected_title + " actual page displayed is: " + self.driver.title)
            return flag
        except TimeoutException:
            print("Application is not navigated to the: " + expected_title +
                  " actual page displayed is: "+ self.driver.title)
            return flag

    @staticmethod
    def get_text(web_element):
        try:
            return web_element.text
        except Exception:
            print("Unable to return the text of an element: "+Exception)
            assert False
