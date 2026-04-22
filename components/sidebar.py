from selenium.webdriver.common.by import By

from components.base_components import BaseComponent

DASHBOARD_BUTTON_LOCATOR = (
    By.XPATH,
    "//a[@role='menuitem' and contains(text(), 'Dashboard')]"
)
TASKS_BUTTON_LOCATOR = (
    By.XPATH,
    "//a[@role='menuitem' and contains(text(), 'Tasks')]"
)
USERS_BUTTON_LOCATOR = (
    By.XPATH,
    "//a[@role='menuitem' and contains(text(), 'Users')]"
)
LABELS_BUTTON_LOCATOR = (
    By.XPATH,
    "//a[@role='menuitem' and contains(text(), 'Labels')]"
)
TASK_STATUSES_BUTTON_LOCATOR = (
    By.XPATH,
    "//a[@role='menuitem' and contains(text(), 'Task statuses')]"
)


class Sidebar(BaseComponent):
    @property
    def dashboard_button(self):
        return self.button(DASHBOARD_BUTTON_LOCATOR)

    @property
    def tasks_button(self):
        return self.button(TASKS_BUTTON_LOCATOR)

    @property
    def users_button(self):
        return self.button(USERS_BUTTON_LOCATOR)

    @property
    def labels_button(self):
        return self.button(LABELS_BUTTON_LOCATOR)

    @property
    def task_statuses_button(self):
        return self.button(TASK_STATUSES_BUTTON_LOCATOR)

    def open_users_page(self):
        self.users_button.click()

    def open_task_statuses_page(self):
        self.task_statuses_button.click()

    def open_labels_page(self):
        self.labels_button.click()

    def open_tasks_page(self):
        self.tasks_button.click()

    def open_dashboard_page(self):
        self.dashboard_button.click()
