from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.utils import wait_for

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
CREATE_BUTTON_LOCATOR = (By.XPATH, "//a[@aria-label='Create']")

TASK_XPATH = ("//div[./h6[contains(text(), '{status}')]]"
              "//div[.//div[contains(text(), '{title}')] and "
              "./p[contains(text(), '{content}')]]/parent::div")
COMBOBOX_OPTION_XPATH = "//li[contains(text(), '{text}')]"
EDIT_BUTTON_XPATH = TASK_XPATH + "//a[@aria-label='Edit']"
STATUS_LABEL_XPATH = "//h6[contains(text(), '{status}')]"


class TasksPage(BasePage):

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
    def create_button(self):
        return self.button(CREATE_BUTTON_LOCATOR)

    def status_label(self, status):
        return self.label((By.XPATH, STATUS_LABEL_XPATH.format(status=status)))

    def task(self, status, title, content):
        return self.table_row((By.XPATH, TASK_XPATH.format(
            status=status, title=title, content=content))
                              )

    def edit_task_button(self, status, title, content):
        return self.button((By.XPATH, EDIT_BUTTON_XPATH.format(
            status=status, title=title, content=content))
                           )

    def open_create_task(self):
        return self.create_button.click()

    def is_task_present(self, status, title, content):
        return self.task(status, title, content).is_present()

    def combobox_option(self, text):
        return self.button((By.XPATH, COMBOBOX_OPTION_XPATH.format(text=text)))

    def select_option(self, text):
        return self.combobox_option(text).click()

    def get_tasks_count(self, status, title, content):
        return len(self.task(status, title, content).find_elements())

    def choose_assignee(self, mail):
        self.assignee_combobox.click()
        wait_for(lambda: self.combobox_option(mail).is_present())
        self.select_option(mail)

    def choose_status(self, status):
        self.status_combobox.click()
        wait_for(lambda: self.combobox_option(status).is_present())
        self.select_option(status)

    def choose_label(self, label):
        self.label_combobox.click()
        wait_for(lambda: self.combobox_option(label).is_present())
        self.select_option(label)

    def open_edit_task(self, status, title, content):
        self.edit_task_button(status, title, content).click()
