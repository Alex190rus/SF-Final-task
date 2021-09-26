import pytest


class Mob_App():

    def __init__(self, driver):
        self.driver = driver

    def get_mob_app(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Персональные рекомендации')]")