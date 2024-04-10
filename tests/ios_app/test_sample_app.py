import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with allure.step('Type search Appium'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type('Appium').press_enter()

    with allure.step('Verify content found'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text('Appium'))
