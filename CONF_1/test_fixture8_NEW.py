import pytest
from selenium import webdriver
link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("\ THIS IS SMOKE TEST .................")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("\ THIS IS REGRESSION TEST .................")

#pytest -s -v --setup-show CONF_1\test_fixture8_NEW.py -p no:warnings