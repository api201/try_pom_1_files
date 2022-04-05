import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print('\n БРАУЗЕР ЕЩЕ НЕ ЗАКРЫЛСЯ. ЖДИТЕ')
    time.sleep(10)
    # этот код выполнится после завершения теста
    print("\n ЗАКРЫЛСЯ БРАУЗЕР. ТЕСТ ЗАВЕРШИТСЯ ЧЕРЕЗ 5 СЕК")
    time.sleep(10)
    print("\n ЗАКРЫВАЮ.........")
    time.sleep(10) #ЗАКРЫВАЕТСЯ ЗДЕСЬ
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    # def test_guest_should_see_basket_link_on_the_main_page(self, browser):
    #     browser.get(link)
    #     browser.find_element_by_css_selector(".basket-mini .btn-group > a")