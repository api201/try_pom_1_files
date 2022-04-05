import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('xlinks', [
    "PassionLinda",
    "NecroLina",
    "roselynax"])

def test_guest_should_see_login_link(browser, xlinks):
    link = f"https://bongacams.com/{xlinks}/"
    browser.get(link)
    close_btn = browser.find_element(By.XPATH, '//*[@id="warning_popup"]/div/div/div[2]/div[4]/a[1]').click()
    time.sleep(2)
    browser.execute_script('''window.open("https://bongacams.com/Sweet-Candy88", "_blank");''')
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)

#https://bongacams.com/NecroLina
#https://bongacams.com/roselynax