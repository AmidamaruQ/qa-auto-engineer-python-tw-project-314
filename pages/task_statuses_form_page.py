from selenium.webdriver.common.by import By

from pages.base_page import BasePage

NAME_INPUT_LOCATOR = (By.XPATH, '//input[@name="name"]')
SLUG_NAME_INPUT_LOCATOR = (By.XPATH, '//input[@name="slug"]')
SAVE_BUTTON_LOCATOR = (By.XPATH, '//button[@aria-label="Save"]')
DELETE_BUTTON_LOCATOR = (By.XPATH, '//button[@aria-label="Delete"]')


class TaskStatusesFormPage(BasePage):
    @property
    def name_input(self):
        return self.input(NAME_INPUT_LOCATOR)

    @property
    def slug_input(self):
        return self.input(SLUG_NAME_INPUT_LOCATOR)

    @property
    def save_button(self):
        return self.button(SAVE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def create_task_status(self, name, slug):
        self.logger.info("Create task status %s, %s", name, slug)
        self.name_input.fill(name)
        self.slug_input.fill(slug)
        self.save_button.click()

    def update_task_status_info(self, name=None, slug=None):
        self.logger.info("Change user %s, %s", name, slug)
        if name is not None:
            self.name_input.fill(name)
        if slug is not None:
            self.slug_input.fill(slug)
        self.save_button.click()

    def delete_task_status(self):
        return self.delete_button.click()