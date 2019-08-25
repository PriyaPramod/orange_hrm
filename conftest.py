import pytest
from source.utilities import helper
from source.utilities.webdriver_manager import start_browser
from source.utilities.properties import ReadConfig


@pytest.fixture(scope='session', autouse=True)
def set_property():
    yield
    ReadConfig.write_to_report()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_"+rep.when, rep)

    return rep


@pytest.fixture(scope='function', autouse=True)
def set_up(request):
    driver = start_browser(ReadConfig.get_browser(), ReadConfig.get_url())

    if request is not None:
        request.node.driver = driver
    yield
    if request.node.rep_call.passed:
        print("Successively executed " + request.function.__name__)
    else:
        helper.attach_screen_shot(driver, request.function.__name__)
    driver.quit()

