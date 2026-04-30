from venv import logger

from pages.base_page import BasePage
from pages.locators.register_locators import RegisterLocators
from utils.logger import get_logger

class RegisterPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        logger = get_logger()

    logger.info("First Script logs")

    def highlight(self, locator):
        self.page.locator(locator).evaluate("el => el.style.border='3px solid red'")

    def fill_form(self, fname, lname, address, email, phone):
        self.fill(RegisterLocators.FIRST_NAME, fname)
        self.fill(RegisterLocators.LAST_NAME, lname)
        self.fill(RegisterLocators.ADDRESS, address)
        self.fill(RegisterLocators.EMAIL, email)
        self.fill(RegisterLocators.PHONE, phone)

        self.click(RegisterLocators.GENDER)
        self.click(RegisterLocators.HOBBY)

        self.click(RegisterLocators.GENDER)
        self.click(RegisterLocators.HOBBY)

    def select_language(self):
        self.click(RegisterLocators.LANGUAGE_BOX)
        elements = self.page.locator(RegisterLocators.LANGUAGE_LIST)

        for i in range(elements.count()):
            text = elements.nth(i).inner_text()
            if "FRENCH" in text.upper():
                elements.nth(i).click()
                self.click(RegisterLocators.CLOSE_LANGUAGE)
                break

    def select_skill(self):
        options = self.page.locator(RegisterLocators.SKILL_OPTIONS)

        for i in range(options.count()):
            text = options.nth(i).inner_text()
            if "UI" in text.upper():
                self.page.locator(RegisterLocators.SKILL_DROPDOWN).select_option(index=i)
                break

    def select_country(self):
        self.click(RegisterLocators.COUNTRY_BOX)
        options = self.page.locator(RegisterLocators.COUNTRY_LIST)

        for i in range(options.count()):
            text = options.nth(i).inner_text()
            if "INDIA" in text.upper():
                options.nth(i).click()
                break

    def select_dob(self):
        self.page.locator(RegisterLocators.YEAR).select_option(value="2001")
        self.page.locator(RegisterLocators.MONTH).select_option(label="January")
        self.page.locator(RegisterLocators.DAY).select_option(index=13)

    def set_password(self, password):
     self.fill(RegisterLocators.PASSWORD, password)
     self.fill(RegisterLocators.REPASSWORD, password)

    def submit_form(self):
        self.click(RegisterLocators.SUBMIT)