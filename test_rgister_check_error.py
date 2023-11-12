from selene import browser, be, have

def test_reg():
    browser.open("https://demowebshop.tricentis.com/")
    browser.element('[href="/register"]').click()
    browser.element('[value="M"]').click()
    browser.element('[id="FirstName"]').send_keys('Viktor')
    browser.element('[id="LastName"]').send_keys('Bukarev')
    browser.element('[id="Email"]').send_keys('Bukarev1985@gmail.com')
    browser.element('[id="Password"]').send_keys('Qwerty1!')
    browser.element('[id="ConfirmPassword"]').send_keys('Qwerty1!')
    browser.element('[id="register-button"]').click()
    browser.element('[class="validation-summary-errors"]').should(have.exact_text('The specified email already exists'))