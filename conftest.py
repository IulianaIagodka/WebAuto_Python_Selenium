import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="D:/Projects/Git_WS/chromedriver_win32/bin/chromedriver.exe")
    yield driver
    driver.quit()