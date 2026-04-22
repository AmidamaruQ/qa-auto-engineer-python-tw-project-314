from pages.dashboard_page import DashboardPage
from pages.label_form_page import LabelFormPage
from pages.labels_page import LabelsPage
from pages.login_page import LoginPage
from pages.task_form_page import TaskFormPage
from pages.task_statuses_form_page import TaskStatusesFormPage
from pages.task_statuses_page import TaskStatusesPage
from pages.tasks_page import TasksPage
from pages.user_form_page import UserFormPage
from pages.users_page import UsersPage


class Pages:
    def __init__(self, driver):
        self.base_page = LoginPage(driver)
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.users_page = UsersPage(driver)
        self.user_form_page = UserFormPage(driver)
        self.tasks_page = TasksPage(driver)
        self.task_statuses_page = TaskStatusesPage(driver)
        self.task_statuses_form_page = TaskStatusesFormPage(driver)
        self.labels_page = LabelsPage(driver)
        self.label_form_page = LabelFormPage(driver)
        self.task_form_page = TaskFormPage(driver)





