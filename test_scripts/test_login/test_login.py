from source.pages.page_manager import get_login, get_dashboard
from source.utilities import excel, constants


class TestLogin:

    def test_tc_001_invalid_login(self, request):
        invalid_user_name = excel.get_cell_value(constants.EXCEL_PATH, "Cart", 0, "InvalidUserName")
        error_message = excel.get_cell_value(constants.EXCEL_PATH, "Cart", 0, "LoginErrorMessage")

        dashboard = get_dashboard(request.node.driver)
        dashboard.hover_on_sign_in()
        dashboard.click_on_sign_in()
        login = get_login(request.node.driver)
        login.enter_email_mobile_number(invalid_user_name)
        login.click_on_continue()

        assert login.get_error_message() in error_message, "Expected error message "+error_message+" is not displaying"


