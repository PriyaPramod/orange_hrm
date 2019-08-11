from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from source.utilities.properties import ReadConfig


class Actions:

    @staticmethod
    def get_action(driver):
        return ActionChains(driver)

    @staticmethod
    def move_to_element(driver, element):
        action = Actions.get_action(driver)
        action.move_to_element(element)
        action.perform()

    @staticmethod
    def action_click(driver, element):
        action = Actions.get_action(driver)
        action.click(element)
        action.perform()


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