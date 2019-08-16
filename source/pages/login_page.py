from selenium.webdriver.common.by import By

from source.pages.base_page import BasePage


class LoginPage(BasePage):

    def __email_text_box(self): return self.find_element(By.CSS_SELECTOR, "#ap_email")
    def __continue_button(self): return self.find_element(By.CSS_SELECTOR, "#continue")
    def __error_message(self): return self.find_element(By.XPATH, "//span[@class='a-list-item']")

    def enter_email_mobile_number(self, email_mobile):
        self.send_keys(self.__email_text_box(), email_mobile)

    def click_on_continue(self):
        self.click(self.__continue_button())

    def get_error_message(self):
        return self.get_text(self.__error_message())
