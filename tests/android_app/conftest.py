import allure
import pytest
from selene import browser
from appium.options.android import UiAutomator2Options
from appium import webdriver
from utils import allure_attach
from config import config


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
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
