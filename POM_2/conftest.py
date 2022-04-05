import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    print("\n CONFTEST.PY IS WORKING NOW...........")
    yield browser
    print("\nquit browser..")
    browser.quit()