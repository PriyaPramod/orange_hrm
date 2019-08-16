from source.pages.dashboard_page import DashboardPage
from source.pages.login_page import LoginPage


def get_login(driver):
    return LoginPage(driver)


def get_dashboard(driver):
    return DashboardPage(driver)