from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from source.utilities.properties import ReadConfig


class Actions:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def move_to_element(self, element):
        self.action.move_to_element(element).perform()

    def action_click(self, element):
        self.action.perform()


class Alert:

    @staticmethod
    def __get_alert(driver):
        wait = WebDriverWait(driver, ReadConfig.get_explicit_wait())
        return wait.until(ec.alert_is_present(), "Alert is not present")

    @staticmethod
    def accept_alert(driver):
        alert = Alert.__get_alert(driver)
        alert.accept()

    @staticmethod
    def dismiss_alert(driver):
        alert = Alert.__get_alert(driver)
        alert.dismiss()

    @staticmethod
    def get_alert_text(driver):
        alert = Alert.__get_alert(driver)
        return alert.text