from selenium.common.exceptions import NoSuchElementException


class BasePage():
    # def __init__(self, browser, url):
    #     self.browser = browser
    #     self.url = url
    #     self.browser.implicitly_wait(5)
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def attributee_error(self, how, what):
        try:
            self.browser.current_url(how, what)
        except (AttributeError):
            return False
        return True
