from selenium.webdriver.common.by import By
import allure
from source.pages.base_page import BasePage
from source.utilities.webelement_extentsion import Actions
from source.utilities.webdriver_extension import switch_to_child_window


class DashboardPage(BasePage):

    def __accounts_list(self): return self.find_element(By.XPATH, "//span[@class='nav-line-2'][contains(text(),'Account & Lists')]")
    def __sign_in_button(self): return self.find_element(By.XPATH, "//span[@class='nav-action-inner']")
    def __search_box(self): return self.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
    def __search_button(self): return self.find_element(By.XPATH, "//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input']")
    def __product_link(self): return self.find_element(By.XPATH, "//span[contains(text(),'OnePlus 7 Pro (Nebula Blue, 8GB RAM, 256GB Storage')]")
    def __add_to_cart_button(self): return self.find_element(By.CSS_SELECTOR, "#add-to-cart-button")
    def __cart_success_message(self): return self.find_element(By.XPATH, "//h1[@class='a-size-medium a-text-bold']")
    def __cart_box(self): return self.find_element(By.CSS_SELECTOR, "#nav-cart")

    @allure.step
    def get_product_name(self):
        return self.get_text(self.__product_link())

    @allure.step
    def click_on_cart_box(self):
        self.click(self.__cart_box())

    @allure.step
    def get_message_after_adding_to_cart(self):
        return self.get_text(self.__cart_success_message())

    @allure.step
    def click_on_add_to_cart(self):
        switch_to_child_window(self.driver)
        self.click(self.__add_to_cart_button())

    @allure.step
    def select_product_to_add_to_cart(self):
        self.click(self.__product_link())

    @allure.step
    def enter_product_name_to_search_box(self, product_name):
        self.send_keys(self.__search_box(), product_name)
        self.click(self.__search_button())

    @allure.step
    def hover_on_sign_in(self):
        Actions(self.driver).move_to_element(self.__accounts_list())

    @allure.step
    def click_on_sign_in(self):
        self.click(self.__sign_in_button())

