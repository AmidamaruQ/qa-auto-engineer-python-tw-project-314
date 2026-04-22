from selenium.webdriver.common.by import By

from pages.base_page import BasePage

USERNAME_INPUT_LOCATOR = (By.XPATH, "//input[@name='username']")
PASSWORD_INPUT_LOCATOR = (By.XPATH, "//input[@name='password']")
SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")


class LoginPage(BasePage):
    @property
    def username_input(self):
        return self.input(USERNAME_INPUT_LOCATOR)

    @property
    def password_input(self):
        return self.input(PASSWORD_INPUT_LOCATOR)

    @property
    def submit_button(self):
        return self.button(SUBMIT_BUTTON_LOCATOR)

    def type_username(self, username):
        self.logger.info("Typing username")
        return self.username_input.fill(username)

    def type_password(self, password):
        self.logger.info("Typing password")
        return self.password_input.fill(password)

    def click_submit(self):
        self.logger.info("Submitting login form")
        return self.submit_button.click()

    def login(self, login, password):
        self.logger.info("Logging in as %s", login)
        self.username_input.fill(login)
        self.password_input.fill(password)
        self.submit_button.click()
        return self
