from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from source.utilities import helper
from source.utilities.properties import ReadConfig


class WebDriverListeners(AbstractEventListener):

    def before_click(self, element, driver):
        wait = WebDriverWait(driver, ReadConfig.get_explicit_wait())
        wait.until(ec.element_to_be_clickable(element))

    def before_change_value_of(self, element, driver):
        element.clear()

    def on_exception(self, exception, driver):
        helper.attach_screen_shot(driver, exception)
