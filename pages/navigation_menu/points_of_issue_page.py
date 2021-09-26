import pytest


class Points_Of_Issue():

    def __init__(self, driver):
        self.driver = driver

    def get_points_of_issue(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Москва')]")