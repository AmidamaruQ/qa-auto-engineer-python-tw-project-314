from pages.labels import LabelsPage
from pages.login import LoginPage
from pages.statuses import StatusesPage
from pages.tasks import TasksPage
from pages.users import UsersPage


class Pages:
    def __init__(self, driver, base_url: str):
        self.login = LoginPage(driver, base_url)
        self.users = UsersPage(driver, base_url)
        self.labels = LabelsPage(driver, base_url)
        self.statuses = StatusesPage(driver, base_url)
        self.tasks = TasksPage(driver, base_url)
