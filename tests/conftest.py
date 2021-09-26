from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def driver():
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")
   pytest.driver = webdriver.Chrome(chrome_options=options)
   pytest.driver.implicitly_wait(5)
   yield
   #pytest.driver.quit()