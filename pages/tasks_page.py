from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import xpath_literal
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
BOARD_COLUMNS_LOCATOR = (By.XPATH, "//h6[normalize-space()]")

COMBOBOX_OPTION_XPATH = "//li[contains(text(), '{text}')]"
STATUS_LABEL_XPATH = "//h6[normalize-space()={status}]"


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
        return self.label((By.XPATH, STATUS_LABEL_XPATH.format(
            status=xpath_literal(status),
        )))

    def _task_xpath(self, status=None, title=None, content=None):
        section_xpath = "//div[./h6]"
        card_conditions = []

        if status:
            section_xpath = (
                f"//div[./h6[normalize-space()={xpath_literal(status)}]]"
            )

        if title:
            card_conditions.append(
                f".//div[normalize-space()={xpath_literal(title)}]"
            )

        if content:
            card_conditions.append(
                f"./p[normalize-space()={xpath_literal(content)}]"
            )

        task_xpath = section_xpath + "//div"

        if card_conditions:
            predicates = " and ".join(card_conditions)
            task_xpath += f"[{predicates}]"

        return task_xpath + "/parent::div"

    def task(self, status=None, title=None, content=None):
        return self.table_row((By.XPATH, self._task_xpath(
            status=status,
            title=title,
            content=content,
        )))

    def edit_task_button(self, status, title, content):
        return self.button((By.XPATH, self._task_xpath(
            status=status,
            title=title,
            content=content,
        ) + "//a[@aria-label='Edit']"))

    def open_create_task(self):
        return self.create_button.click()

    def is_task_present(self, status, title, content):
        return self.task(status, title, content).is_displayed()

    def combobox_option(self, text):
        return self.button((By.XPATH, COMBOBOX_OPTION_XPATH.format(text=text)))

    def select_option(self, text):
        return self.combobox_option(text).click()

    def get_tasks_count(self, status=None, title=None, content=None):
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

    def get_board_columns(self):
        return [
            column.text.strip()
            for column in self.driver.find_elements(*BOARD_COLUMNS_LOCATOR)
            if column.text.strip()
        ]

    def get_task_text(self, status, title=None, content=None):
        return self.task(status=status, title=title, content=content).text
