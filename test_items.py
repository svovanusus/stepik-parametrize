link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_should_contain_add_to_cart_button(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket") != None, "Button is not existed!"
