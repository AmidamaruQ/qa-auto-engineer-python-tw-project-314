from components.base_components import BaseComponent
from components.header import Header
from components.popup import Popup
from components.sidebar import Sidebar
from utils import get_logger


class BasePage(BaseComponent):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
        self.sidebar = Sidebar(driver)
        self.popup = Popup(driver)
        self.logger = get_logger(self.__class__.__name__)

    def open(self, url):
        self.logger.info("Opening page: %s", url)
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url
