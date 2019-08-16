from source.pages.page_manager import get_login, get_dashboard


class TestLogin:

    def test_tc_001_invalid_login(self, request):
        dashboard = get_dashboard(request.node.driver)
        dashboard.hover_on_sign_in()
        dashboard.click_on_sign_in()
        login = get_login(request.node.driver)
        login.enter_email_mobile_number("gsakjdhgasdjf")
        login.click_on_continue()

        assert login.get_error_message() in "We cannot find an account with that email address"


