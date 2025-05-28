# base_test.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 15)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

    def navigate_to_home(self):
        self.driver.get("https://e-commerce-for-testing.onrender.com/")
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def navigate_to_login_page(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
        login_button.click()
        self.wait.until(EC.url_contains("/signin"))
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(.,'Sign In')]")))

    def assert_user_logged_in(self):
        try:
            profile_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Profile']")))
            self.assertTrue(profile_button.is_displayed(), "Nút 'Profile' không hiển thị.")
        except TimeoutException:
            self.fail("❌ Không tìm thấy nút Profile.")

    def assert_user_logged_out(self):
        try:
            login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Login']")))
            register_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Register']")))
            self.assertTrue(login_button.is_displayed() and register_button.is_displayed())
        except TimeoutException:
            self.fail("❌ Không tìm thấy nút Login/Register.")

    def register_new_user(self, email, password):
        self.navigate_to_home()
        register_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']")))
        register_button.click()
        self.wait.until(EC.url_contains("/signup"))

        inputs = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//form//input")))
        email_input, password_input, confirm_input = inputs[:3]

        email_input.clear()
        password_input.clear()
        confirm_input.clear()
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_input.send_keys(password)

        sign_up_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign Up']")))
        sign_up_button.click()

        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert.accept()
        except TimeoutException:
            pass

        self.wait.until(EC.url_contains("/signin"))

    def login_user(self, email, password):
        self.navigate_to_login_page()
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))

        email_input.clear()
        password_input.clear()
        email_input.send_keys(email)
        password_input.send_keys(password)

        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign In']")))
        sign_in_button.click()

        self.assert_user_logged_in()

    def logout_user(self):
        self.navigate_to_home()
        profile_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Profile']")))
        profile_button.click()
        logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Logout']")))
        logout_button.click()
        self.wait.until(EC.url_matches(r"https://e-commerce-for-testing\.onrender\.com/?$"))
        self.assert_user_logged_out()

    def add_to_basket(self):
        products = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div")))
        products[0].click()
        add_to_basket_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to Basket')]")))
        add_to_basket_button.click()
        time.sleep(2)

    def open_basket(self):
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Basket')]")))
        cart_button.click()
        time.sleep(2)

    def add_and_remove_product_in_cart(self):
        self.navigate_to_home()
        self.add_to_basket()
        self.open_basket()

        remove_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Remove from Basket')]")))
        remove_button.click()
        time.sleep(2)

        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'Your cart is empty')] | //div[contains(text(),'Your cart is empty')]")
        ))
