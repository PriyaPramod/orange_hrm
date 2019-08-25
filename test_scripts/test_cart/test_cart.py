from source.utilities import excel, constants
from source.pages import page_manager as pm


class TestCart:

    def test_tc_002_add_product_and_verify(self, request):
        product_name = excel.get_cell_value(constants.EXCEL_PATH, "Cart", 1, "ProductName")
        success_message = excel.get_cell_value(constants.EXCEL_PATH, "Cart", 1, "SuccessMessage")
        success_message_after_deleting = excel.get_cell_value(constants.EXCEL_PATH, "Cart", 1, "SuccessMessageAfterDelete")

        dashboard = pm.get_dashboard(request.node.driver)
        cart = pm.get_cart(request.node.driver)

        dashboard.enter_product_name_to_search_box(product_name)
        product_added = dashboard.get_product_name()
        dashboard.select_product_to_add_to_cart()

        dashboard.click_on_add_to_cart()
        message = dashboard.get_message_after_adding_to_cart()

        assert success_message in message, "Unable to add the product to cart"

        dashboard.click_on_cart_box()
        product_name_in_cart = cart.get_product_name_from_cart_page()

        assert product_name_in_cart == product_added, "Added product is not available in the cart page"

        cart.delete_the_added_product_from_cart()

        assert cart.get_confirm_message_after_deleting_product() in success_message_after_deleting
