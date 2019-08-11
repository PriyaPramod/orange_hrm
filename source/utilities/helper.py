import allure


def attach_screen_shot(driver, name):
    allure.attach(driver.get_screenshot_as_png(), name,
                  attachment_type=allure.attachment_type.PNG)