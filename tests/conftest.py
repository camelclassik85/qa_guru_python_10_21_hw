import allure
import pytest
from appium.options.ios import XCUITestOptions
from selene import browser
from appium.options.android import UiAutomator2Options
from appium import webdriver
from utils import allure_attach
from config import config


@allure.step('Select platform according running test folder')
def pytest_addoption(parser):
    parser.addoption('--platform')


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    platform = request.config.getoption("--platform")
    try:
        platform = platform.lower()
    except AttributeError:
        with allure.step('Absent --platform=value in start test command'):
            raise ValueError('Absent --platform=value in start test command')
    if 'android' in platform.lower():
        with allure.step('Android driver config create'):
            options = UiAutomator2Options().load_capabilities({
                "platformName": "android",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",

                "app": "bs://sample.app",

                'bstack:options': {
                    "projectName": "Android app Python project",
                    "buildName": "android-browserstack-build",
                    "sessionName": "Android",

                    "userName": config.user_name,
                    "accessKey": config.access_key
                }
            })
    elif 'ios' in platform.lower():
        with allure.step('IOS driver config create'):
            options = XCUITestOptions().load_capabilities({
                "deviceName": "iPhone XS",
                "platformName": "ios",
                "platformVersion": "12",

                "app": "bs://sample.app",

                'bstack:options': {
                    "projectName": "IOS app Python project",
                    "buildName": "ios-browserstack-build",
                    "sessionName": "IOS",

                    "userName": config.user_name,
                    "accessKey": config.access_key
                }
            })
    else:
        with allure.step('Incorrect --platform value in start test command'):
            raise ValueError('Incorrect --platform value in start test command')

    browser.config.driver = webdriver.Remote(config.base_url, options=options)
    browser.config.timeout = config.timeout

    yield

    session_id = browser.driver.session_id

    with allure.step('Add screenshot'):
        allure_attach.attach_screenshot(browser)

    with allure.step('Add html'):
        allure_attach.attach_xml(browser)

    with allure.step('tear down app session'):
        browser.quit()

    with allure.step('Add video'):
        allure_attach.attach_video(session_id)
