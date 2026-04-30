import pytest
import allure
from playwright.sync_api import sync_playwright
from utils.config import Config


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # Browser selection
        if Config.BROWSER == "chromium":
            browser = p.chromium.launch(headless=Config.HEADLESS,slow_mo=500)
        elif Config.BROWSER == "firefox":
            browser = p.firefox.launch(headless=Config.HEADLESS)
        elif Config.BROWSER == "webkit":
            browser = p.webkit.launch(headless=Config.HEADLESS)
        else:
            raise Exception("Invalid browser")

        context = browser.new_context(
            viewport={"width": Config.VIEWPORT_WIDTH, "height": Config.VIEWPORT_HEIGHT},
            screen={"width": Config.VIEWPORT_WIDTH, "height": Config.VIEWPORT_HEIGHT}
        )
        page = context.new_page()

        yield page

        context.close()
        browser.close()


   
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )