from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import xpath_literal

CREATE_BUTTON_LOCATOR = (By.XPATH, "//a[@aria-label='Create']")
DELETE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Delete']")
TABLE_HEADERS_LOCATOR = (By.XPATH, "//thead//th")
TABLE_ROWS_LOCATOR = (By.XPATH, "//tbody/tr")

ROW_WITH_CURRENT_DATA_XPATH = ("//tr[.//*[normalize-space()={email}] "
                               "and .//*[normalize-space()={first_name}] "
                               "and .//*[normalize-space()={second_name}]]"
                               )
ROW_WITH_EMAIL_XPATH = "//tr[.//*[normalize-space()={email}]]"
CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH = (ROW_WITH_CURRENT_DATA_XPATH
                                        + "//td[.//input[@type='checkbox']]")


class UsersPage(BasePage):

    @property
    def create_button(self):
        return self.button(CREATE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def _checkbox_user_row(self, email, first_name, second_name):
        return self.input(
            (By.XPATH, CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH.format(
                email=xpath_literal(email),
                first_name=xpath_literal(first_name),
                second_name=xpath_literal(second_name))))

    def _user_row(self, email, first_name, second_name):
        return self.table_row((By.XPATH, ROW_WITH_CURRENT_DATA_XPATH.format(
            email=xpath_literal(email),
            first_name=xpath_literal(first_name),
            second_name=xpath_literal(second_name))))

    def _user_row_by_email(self, email):
        return self.table_row((By.XPATH, ROW_WITH_EMAIL_XPATH.format(
            email=xpath_literal(email),
        )))

    def open_create_user_form(self):
        return self.create_button.click()

    def is_user_present(self, email, first_name, second_name):
        return self._user_row(email, first_name, second_name).is_present()

    def open_user_from_table(self, email, first_name, second_name):
        return self._user_row(email, first_name, second_name).click()

    def choose_user_in_table(self, email, first_name, second_name):
        return self._checkbox_user_row(email, first_name, second_name).click()

    def delete_chosen_user(self):
        return self.delete_button.click()

    def get_table_headers(self):
        return [
            header.text.strip()
            for header in self.driver.find_elements(*TABLE_HEADERS_LOCATOR)
            if header.text.strip()
        ]

    def get_users_count(self):
        return len(self.driver.find_elements(*TABLE_ROWS_LOCATOR))

    def get_user_row_text(self, email):
        return self._user_row_by_email(email).text
