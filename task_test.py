import unittest
import xmlrunner
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TaksTest(unittest.TestCase):
    URL = "http://testarena.pl/demo"
    LOGIN = "administrator@testarena.pl"
    PASS = "sumXQQ72$L"
    EXPECTED_URL = "http://demo.testarena.pl/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get(self.URL)
        driver.maximize_window()


    def test_login(self):

        self.login(self.LOGIN, self.PASS)

        assert self.driver.current_url == self.EXPECTED_URL, "Nie poprawny url po zalogowaniu"


    def test_wrong_login(self):
        wait = WebDriverWait(self.driver, 10)
        self.login("wrong_login", "wrong_pass")

        message_error_div = self.driver.find_element(By.CSS_SELECTOR, "div.login_form_error")

        assert  message_error_div.is_displayed(), "Brak elementu z komunikaten błędu"


    def login(self, login: str, password: str):
        wait = WebDriverWait(self.driver, 10)
        button_click = wait.until(EC.presence_of_element_located(
            (By.XPATH, ".//a[@class='btn btn-fill btn-primary' and @href='http://demo.testarena.pl/']")))
        button_click.click()

        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])

        input_login = wait.until(EC.presence_of_element_located((By.ID, "email")))
        input_login.send_keys(login)

        input_password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
        input_password.send_keys(password)

        button_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login")))
        button_login.click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report.html'))