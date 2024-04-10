import allure
import pytest
from selene import browser
from appium.options.android import UiAutomator2Options
from appium import webdriver
from utils.constants import config


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": config.user_name,
            "accessKey": config.access_key
        }
    })

    # browser.config.driver = webdriver.Remote(BASE_URL, options=options)
    browser.config.driver_remote_url = config.base_url
    browser.config.driver_options = options

    browser.config.timeout = config.timeout

    yield

    with allure.step('tear down app session'):
        browser.quit()
