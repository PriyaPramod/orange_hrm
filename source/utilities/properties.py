import sys
from pyjavaproperties import Properties
from source.utilities import constants


class ReadConfig:

    @staticmethod
    def get_properties():
        prop = Properties()
        prop.load(open(constants.PROPERTIES_PATH, mode='r'))
        return prop

    @staticmethod
    def get_url():
        prop = ReadConfig.get_properties()
        return prop.getProperty("ApplicationURL")

    @staticmethod
    def get_browser():
        prop = ReadConfig.get_properties()
        return prop.getProperty("Browser")

    @staticmethod
    def get_implicit_wait():
        prop = ReadConfig.get_properties()
        return int(prop.getProperty("IWait"))

    @staticmethod
    def get_explicit_wait():
        prop = ReadConfig.get_properties()
        return int(prop.getProperty("EWait"))

    @staticmethod
    def write_to_report():
        prop = ReadConfig.get_properties()
        out = open(constants.ALLURE_RESULTS + "environment.properties", mode='w')
        prop.setProperty("Browser Name", ReadConfig.get_browser())
        prop.setProperty("Application URL", ReadConfig.get_url())
        prop.setProperty("Python version", str(sys.version))
        prop.setProperty("Platform", str(sys.getwindowsversion()))
        prop.store(out)