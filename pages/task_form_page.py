from selenium.webdriver.common.by import By

from pages.base_page import BasePage

ASSIGNEE_COMBOBOX_LOCATOR = (
    By.XPATH,
    "//div[div/following-sibling::input[@name='assignee_id']]"
)
STATUS_COMBOBOX_LOCATOR = (
    By.XPATH,
    "//div[div/following-sibling::input[@name='status_id']]"
)
LABEL_COMBOBOX_LOCATOR = (
    By.XPATH,
    "//div[div/following-sibling::input[@name='label_id']]"
)
TITLE_INPUT_LOCATOR = (By.XPATH, "//input[@name='title']")
CONTENT_INPUT_LOCATOR = (By.XPATH, "//textarea[@name='content']")
SAVE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Save']")
DELETE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Delete']")

COMBOBOX_OPTION_XPATH = "//li[contains(text(), '{text}')]"


class TaskFormPage(BasePage):

    @property
    def assignee_combobox(self):
        return self.combobox(ASSIGNEE_COMBOBOX_LOCATOR)

    @property
    def status_combobox(self):
        return self.combobox(STATUS_COMBOBOX_LOCATOR)

    @property
    def label_combobox(self):
        return self.combobox(LABEL_COMBOBOX_LOCATOR)

    @property
    def title_input(self):
        return self.input(TITLE_INPUT_LOCATOR)

    @property
    def content_input(self):
        return self.input(CONTENT_INPUT_LOCATOR)

    @property
    def save_button(self):
        return self.button(SAVE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def combobox_option(self, text):
        return self.button((By.XPATH, COMBOBOX_OPTION_XPATH.format(text=text)))

    def select_option(self, text):
        return self.combobox_option(text).click()

    def save_task(self):
        self.save_button.click()

    def create_task(self, assignee, title, status, label, content):
        self.assignee_combobox.click()
        self.select_option(assignee)
        self.title_input.fill(title)
        self.content_input.fill(content)
        self.status_combobox.click()
        self.select_option(status)
        self.label_combobox.click()
        self.select_option(label)
        self.assignee_combobox.close_combobox()
        self.save_task()

    def update_task(self,
                    assignee=None,
                    title=None,
                    status=None,
                    label=None,
                    content=None):
        if assignee is not None:
            self.assignee_combobox.click()
            self.select_option(assignee)
        if title is not None:
            self.title_input.fill(title)
        if status is not None:
            self.status_combobox.click()
            self.select_option(status)
        if content is not None:
            self.content_input.fill(content)
        if label is not None:
            self.label_combobox.click()
            self.select_option(label)
            self.assignee_combobox.close_combobox()
        self.save_task()

    def delete_task(self):
        self.delete_button.click()
