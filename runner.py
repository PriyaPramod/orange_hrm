import pytest
import os
from source.utilities import constants
from datetime import datetime


class ReportPlugin:
    def pytest_sessionfinish(self):
        allure_report_folder = constants.ALLURE_REPORT + datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        command = "allure generate "+constants.ALLURE_RESULTS + " --output " + allure_report_folder
        os.popen(command)


arguments = ["-q", "--alluredir", constants.ALLURE_RESULTS]
pytest.main(arguments, plugins=[ReportPlugin()])