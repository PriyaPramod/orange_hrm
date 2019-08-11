from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(30)
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def send_keys(self, element, value):
        element.send_keys(value)

    def verify_title(self, expected_title):
        flag = False
        try:
            flag = self.wait.until(ec.title_contains(expected_title),
                "Application is not navigated to the: " + expected_title +
                            " actual page displayed is: " + self.driver.title)
            return flag
        except TimeoutException:
            print("Application is not navigated to the: " + expected_title +
                  " actual page displayed is: "+ self.driver.title)
            return flag

