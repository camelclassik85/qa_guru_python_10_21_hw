import allure
import requests
from config import config


def attach_screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )


def attach_xml(browser):
    allure.attach(
        body=browser.driver.page_source,
        name='screen XML dump',
        attachment_type=allure.attachment_type.XML
    )


def attach_video(session_id):
    # user_name = os.getenv('USER_NAME')
    # access_key = os.getenv('ACCESS_KEY')
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.user_name, config.access_key),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
