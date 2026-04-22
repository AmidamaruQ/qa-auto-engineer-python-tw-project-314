from selenium.webdriver.common.by import By

from pages.base_page import BasePage

NAME_INPUT_LOCATOR = (By.XPATH, '//input[@name="name"]')
SAVE_BUTTON_LOCATOR = (By.XPATH, '//button[@aria-label="Save"]')
DELETE_BUTTON_LOCATOR = (By.XPATH, '//button[@aria-label="Delete"]')


class LabelFormPage(BasePage):
    @property
    def name_input(self):
        return self.input(NAME_INPUT_LOCATOR)

    @property
    def save_button(self):
        return self.button(SAVE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def create_label(self, name):
        self.logger.info("Create label %s", name)
        self.name_input.fill(name)
        self.save_button.click()

    def update_label_info(self, name):
        self.logger.info("Change label %s", name)
        self.name_input.fill(name)
        self.save_button.click()

    def delete_label(self):
        return self.delete_button.click()