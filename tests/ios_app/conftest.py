import allure
import pytest
from appium.options.ios import XCUITestOptions
from selene import browser
from appium import webdriver
from utils import allure_attach
from config import config


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities({
        "deviceName": "iPhone XS",
        "platformName": "ios",
        "platformVersion": "12",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "Second Python project",
            "buildName": "browserstack-build-2",
            "sessionName": "BStack second_test",

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
