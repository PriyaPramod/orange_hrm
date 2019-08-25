from selenium.webdriver.common.by import By
import allure
from source.pages.base_page import BasePage


class CartPage(BasePage):

    def __product_name(self): return self.find_element(By.XPATH, "//span[@class='a-size-medium sc-product-title a-text-bold']")
    def __delete_product_button(self): return self.find_element(By.CSS_SELECTOR, "input[name^='submit.delete']")
    def __delete_confirm_message(self): return self.find_element(By.CSS_SELECTOR, "div[data-action='delete'] a.a-link-normal.sc-product-link")

    @allure.step
    def get_confirm_message_after_deleting_product(self):
        return self.get_text(self.__delete_confirm_message())

    @allure.step
    def get_product_name_from_cart_page(self):
        return self.get_text(self.__product_name())

    @allure.step
    def delete_the_added_product_from_cart(self):
        self.click(self.__delete_product_button())

