from selenium.webdriver.common.by import By

from source.pages.base_page import BasePage
from source.utilities.webelement_extentsion import Actions


class DashboardPage(BasePage):

    def __accounts_list(self): return self.find_element(By.XPATH, "//span[@class='nav-line-2'][contains(text(),'Account & Lists')]")
    def __sign_in_button(self): return self.find_element(By.XPATH, "//span[@class='nav-action-inner']")

    def hover_on_sign_in(self):
        Actions(self.driver).move_to_element(self.__accounts_list())

    def click_on_sign_in(self):
        self.click(self.__sign_in_button())

