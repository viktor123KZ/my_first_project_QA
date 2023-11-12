import time
from selenium import webdriver
import pytest
from selene import browser
from selene import have, be


a = 'Bukarev Viktor Vladimirovich'
e = 'bukarev1985@gmail.com'
address = '1, testovaya str, Almaty, Kazakhstan'
address2 = '2, testovaya str, Almaty, Kazakhstan'

@pytest.fixture
def size_windows():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1400,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    browser.config.driver_options = options
    return browser



def test1(size_windows):
    browser.open('https://demoqa.com/text-box')
    browser.element('[id="userName"]').type(a)
    browser.element('[id="userEmail"]').type(e)
    browser.element('//*[@id="currentAddress-wrapper"]/div[2] //*[@id="currentAddress"]').type(address)
    browser.element('//*[@id="permanentAddress-wrapper"]/div[2] //*[@id="permanentAddress"]').type(address2)
    browser.execute_script("window.scrollTo(0, 1080)")
    browser.element('//*[@id="submit"]').click()
    browser.element('//*[@id="name"]').should(have.exact_text('Name:Bukarev Viktor Vladimirovich'))
    browser.element('//*[@id="email"]').should(have.exact_text('Email:bukarev1985@gmail.com'))
    browser.element('//*[@id="output"]/div //*[@id="currentAddress"]').should(have.exact_text('Current Address :1, testovaya str, Almaty, Kazakhstan'))
    browser.element('//*[@id="output"] //*[@id="permanentAddress"]').should(have.exact_text('Permananet Address :2, testovaya str, Almaty, Kazakhstan'))
    time.sleep(4)

def test_example(size_windows):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_valid_login(size_windows):
    browser.open('https://demowebshop.tricentis.com/')
    browser.element('[class="ico-login"]').click()
    browser.element('[id="Email"]').type('Bukarev1985@gmail.com')
    browser.element('[id="Password"]').type('Qwerty1!')
    browser.element('.form-fields .button-1').click()
    browser.element('.header .account').should(have.exact_text('Bukarev1985@gmail.com'))
    browser.element('[class="ico-logout"]').click()
    browser.element('[class="ico-login"]').should(have.exact_text('Log in'))
