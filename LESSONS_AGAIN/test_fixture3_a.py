import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    print('\n НАЧИНАЮ ВЫПОЛНЯТЬ ТЕСТ')
    time.sleep(10)
    yield browser

    # этот код выполнится после завершения теста
    print("\n ТЕСТ ПРОЙДЕН, НО БРАУЗЕР ЕЩЕ НЕ ЗАКРЫТ")
    time.sleep(10)
    print("\n ЗАКРЫВАЮ.........")
    time.sleep(5) #ЗАКРЫВАЕТСЯ ЗДЕСЬ
    browser.quit()
    print("\n ОК ЗАКРЫЛ.........")
    time.sleep(5)

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    # def test_guest_should_see_basket_link_on_the_main_page(self, browser):
    #     browser.get(link)
    #     browser.find_element_by_css_selector(".basket-mini .btn-group > a")