from selene import browser, have

import time

def test_valid_login():
    browser.open('https://demowebshop.tricentis.com/')
    browser.element('[class="ico-login"]').click()
    browser.element('[id="Email"]').type('Bukarev1985@gmail.com')
    browser.element('[id="Password"]').type('Qwerty1!')
    browser.element('//*[@class="returning-wrapper"] //*[@type="submit"]').click()
    time.sleep(1)
    browser.element('.header .account').should(have.exact_text('Bukarev1985@gmail.com'))
    browser.element('[class="ico-logout"]').click()
    browser.element('[class="ico-login"]').should(have.exact_text('Log in'))
