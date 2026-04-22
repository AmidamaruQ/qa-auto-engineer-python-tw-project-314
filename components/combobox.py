from selenium.webdriver import ActionChains, Keys

from elements import BaseElement


class Combobox(BaseElement):
    def close_combobox(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()