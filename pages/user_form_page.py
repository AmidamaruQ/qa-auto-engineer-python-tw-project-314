from selenium.webdriver.common.by import By

from pages.base_page import BasePage

EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[@name="email"]')
FIRST_NAME_INPUT_LOCATOR = (By.XPATH, '//input[@name="firstName"]')
LAST_NAME_INPUT_LOCATOR = (By.XPATH, '//input[@name="lastName"]')
SAVE_BUTTON_LOCATOR = (By.XPATH, '//button[@aria-label="Save"]')
DELETE_BUTTON_LOCATOR = (By.XPATH, '//button[@aria-label="Delete"]')


class UserFormPage(BasePage):
    @property
    def email_input(self):
        return self.input(EMAIL_INPUT_LOCATOR)

    @property
    def first_name_input(self):
        return self.input(FIRST_NAME_INPUT_LOCATOR)

    @property
    def last_name_input(self):
        return self.input(LAST_NAME_INPUT_LOCATOR)

    @property
    def save_button(self):
        return self.button(SAVE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def create_user(self, email, first_name, last_name):
        self.logger.info("Create user %s, %s, %s", email, first_name, last_name)
        self.email_input.fill(email)
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.save_button.click()

    def update_user_info(self, email=None, first_name=None, last_name=None):
        self.logger.info("Change user %s, %s, %s", email, first_name, last_name)
        if email is not None:
            self.email_input.fill(email)
        if first_name is not None:
            self.first_name_input.fill(first_name)
        if last_name is not None:
            self.last_name_input.fill(last_name)
        self.save_button.click()

    def delete_user(self):
        return self.delete_button.click()
